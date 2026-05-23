# Scenario Import Format

Supported archive shape:

```text
scenario.zip
├── scenario.yaml
├── media/
│   ├── image.png
│   ├── video.mp4
│   └── document.pdf
└── ai_agents/
    ├── journalist.md
    ├── customer.md
    └── employee.md
```

`scenario.yaml` contains scenario metadata and stimulus rows. Media and AI agent
personas are referenced by relative path.
