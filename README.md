# Paleontology Analysis Tools

Advanced software tools for fossil identification, permineralized dinosaur remains analysis, and paleontological data processing with AI-powered image recognition.

## Features

- **AI-Powered Fossil Identification**: Automated classification of fossil types
- **Image Analysis**: Advanced image processing for fossil specimens
- **Age Estimation**: Geological period and age estimation
- **Preservation Quality Assessment**: Evaluate fossil preservation state
- **Batch Processing**: Analyze multiple specimens simultaneously
- **Data Export**: Export results in JSON or CSV format
- **Species Suggestion**: Database of potential species matches

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/Garrettc123/paleontology-analysis-tools.git
cd paleontology-analysis-tools

# Install dependencies
pip install -r requirements.txt
```

## Usage

### Analyze Single Fossil Image

```bash
python fossil_analyzer.py --image path/to/fossil.jpg
```

### Batch Analysis

```bash
python fossil_analyzer.py --directory path/to/fossil/images
```

### Export Results

```bash
# Export as JSON (default)
python fossil_analyzer.py --image fossil.jpg --output results.json

# Export as CSV
python fossil_analyzer.py --directory fossils/ --output results.csv --format csv
```

## Quick Start Example

```python
from fossil_analyzer import FossilAnalyzer

# Initialize analyzer
analyzer = FossilAnalyzer()

# Analyze single image
result = analyzer.analyze_image('fossil.jpg')
print(result['classification'])

# Batch analyze
results = analyzer.batch_analyze('fossils_directory/')

# Export results
analyzer.export_results('output.json')
```

## Supported Fossil Types

- **Permineralized Bones**: Dinosaur and prehistoric animal bones
- **Petrified Wood**: Ancient tree specimens  
- **Shell Fragments**: Marine invertebrate fossils
- **Trace Fossils**: Footprints and burrows
- **Amber Inclusions**: Organisms preserved in resin

## Analysis Output

Comprehensive data including:
- Fossil type classification
- Geological period estimation
- Age range (millions of years)
- Preservation quality score
- Possible species matches
- Confidence levels

## Command Line Options

```
-i, --image        Path to single fossil image
-d, --directory    Directory containing multiple images
-o, --output       Output file path (default: results.json)
-f, --format       Output format: json or csv
```

## Best Practices

### Image Quality
- Minimum 1024x768 pixels
- Even, diffused lighting
- Plain background
- Sharp focus
- Include scale reference

## License

MIT License

## Author

Garrettc123

## Disclaimer

Preliminary analysis for educational purposes. Professional consultation recommended for official identification.
