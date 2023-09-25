
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
procColor["Detect Color"]
procShape["Detect Shape"]
procTime["Create Timestamp"]
end

subgraph Output
outLog["Logging (CSV)"]
end

inputTime --> procTime
inputImage --> procColor
inputImage --> procShape

procTime --> outLog
procColor --> outLog
procShape --> outLog

```
