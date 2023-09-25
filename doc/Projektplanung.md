
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

## Mermaid
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
