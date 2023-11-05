
# Anforderungen
- Bild einlesen
- Fenster generieren und Bild anzeigen
- Erkennen von Formen: Rechteck, Quadrat, Dreieck, Kreis und Farben:  Rot, Grün, Gelb, Blau, Violett
- Formen umranden und beschriften
- Bild anzeigen
- Logging
  - Timestamp
  - Shape
  - Color
  - Ouptut as CSV

## Input-Processor-Output Diagram
```mermaid
flowchart LR

subgraph Input
inputImage["Image"]
inputTime["Time"]
end

subgraph Processor
procShape["Detect Shapes"]
procTime["Create Timestamp"]
procColor["Detect Color"]
procLog["Logger"]
end

subgraph Output 
outLog["Logging (CSV)"]
outDisplay["Display"]
end


inputTime --> procTime
inputImage --> procShape

procTime --> procLog
procColor --> procLog
procColor --> outDisplay
procShape --> procColor

procLog --> outLog
```

## Component Diagram

```mermaid
flowchart LR

%% BLOBS
processor(("Processor"))
camera(("Camera"))
image(("Image Processor"))
display(("Display"))
logger(("Logger"))

%% LINKS
processor <---> |read Image| camera
processor ---> |send image| image
image ---> |send result| processor
processor ---> |display result| display
processor ---> |log result| logger

```

## Sequence Diagram
```mermaid
sequenceDiagram
autonumber

activate Processor

Processor ->> Camera: Request Image
activate Camera
Camera ->> Processor: Send Image
deactivate Camera

Processor ->> Image Processor: Send Image
activate Image Processor
Image Processor ->> Image Processor: Process Image & Create Timestamp
Image Processor ->> Processor: Send Result
deactivate Image Processor

Processor ->> Display: Send Image & Result
activate Display
Display ->> Display: Display Image & Result
deactivate Display

opt When new result received
  Processor ->> Logger: Send Result
  activate Logger
  Logger ->> Logger: Log Result
  deactivate Logger
end

deactivate Processor
```

## Classes
```mermaid
 classDiagram

      class Camera{
        +requestImage(): cv2:Mat || None
        +requestSample(string path): cv2:Mat || None
        +showImage(cv2.Mat img)
        +release()
      }

      ImageProcessor <|-- DetectShape
      class ImageProcessor{
          +processImage(cv2.Mat frame): Shape Array
          -createTimestamp()
      }

      DetectShape <|-- DetectColor
      class DetectShape{
        +detectShapes(): list
      }

      Shape <|-- Circle
      Shape <|-- Polygon

      class Points{
        dist(): float
	    asarray(): np.array
	    is_intersect(): bool
        +x: float || int
        +y: float || int
      }
      class Shape{
        <<abstract>>
        +getName(): string
        +color: string
      }
      class Circle{
        +getCenter(): string
        +getName(): string
        +fradius: float
        +origin: Point
      }
      class Polygon{
        +getCenter(): string
        +getName(): string
        +getContour(): np.array
        +points: Point Array
      }

      class DetectColor{
          +detectColor(): string
          -hue_to_color(float): string
      }

      class Display{
          +drawContours()
          +name: string
          +ms_wait: int
          +alive: bool
      }

      class Logger{
          <<abstract>>
		  +info(string)
		  +file: string
		  +append_existing: bool
		  +output_terminal: bool
		  +head: string
      }

	  Logger <|-- ShapeLogger

      class ShapeLogger{
		  +log_shapes(Shape List)
	      +shapes: Shape List
      }

```