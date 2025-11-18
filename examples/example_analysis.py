#!/usr/bin/env python3
"""Example fossil analysis workflow"""

from fossil_analyzer import FossilAnalyzer
import json

def main():
    print("Fossil Analysis Example")
    print("=" * 50)
    
    # Initialize analyzer
    analyzer = FossilAnalyzer()
    
    # Example 1: Single image analysis
    print("\nExample 1: Single Image Analysis")
    print("-" * 50)
    # result = analyzer.analyze_image('path/to/fossil.jpg')
    # print(json.dumps(result, indent=2))
    
    # Example 2: Batch processing
    print("\nExample 2: Batch Processing")
    print("-" * 50)
    # results = analyzer.batch_analyze('fossils/')
    # print(f"Processed {len(results)} images")
    
    # Example 3: Export results
    print("\nExample 3: Export Results")
    print("-" * 50)
    # analyzer.export_results('results.json', format='json')
    # analyzer.export_results('results.csv', format='csv')
    
    print("\nPlace your fossil images in the project directory")
    print("Then run: python fossil_analyzer.py --image your_fossil.jpg")

if __name__ == "__main__":
    main()
