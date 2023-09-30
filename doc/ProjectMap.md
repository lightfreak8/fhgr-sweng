
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

opt When new data received
  Processor ->> Logger: Send Result
  activate Logger
  Logger ->> Logger: Log Result
  deactivate Logger
end

deactivate Processor
```
