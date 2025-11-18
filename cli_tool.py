#!/usr/bin/env python3
"""Command-line interface for fossil analysis"""

import sys
import argparse
from pathlib import Path
from fossil_analyzer import FossilAnalyzer
import json


def main():
    parser = argparse.ArgumentParser(
        description="Paleontology Analysis CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze fossil image(s)')
    analyze_parser.add_argument('path', help='Image file or directory')
    analyze_parser.add_argument('-o', '--output', default='results.json', help='Output file')
    analyze_parser.add_argument('-f', '--format', choices=['json', 'csv'], default='json')
    
    # Info command
    info_parser = subparsers.add_parser('info', help='Show system information')
    
    # Database command
    db_parser = subparsers.add_parser('database', help='Species database operations')
    db_parser.add_argument('action', choices=['list', 'search'], help='Database action')
    db_parser.add_argument('query', nargs='?', help='Search query')
    
    args = parser.parse_args()
    
    if args.command == 'analyze':
        analyzer = FossilAnalyzer()
        path = Path(args.path)
        
        if path.is_file():
            result = analyzer.analyze_image(str(path))
            print(json.dumps(result, indent=2))
        elif path.is_dir():
            results = analyzer.batch_analyze(str(path))
            print(f"Analyzed {len(results)} images")
        
        analyzer.export_results(args.output, args.format)
        print(f"Results saved to {args.output}")
    
    elif args.command == 'info':
        print("Paleontology Analysis Tools v1.0")
        print("Supported formats: JPEG, PNG, BMP, TIFF")
        print("Analysis features: Classification, Age Estimation, Preservation Assessment")
    
    elif args.command == 'database':
        with open('database/species_database.json', 'r') as f:
            db = json.load(f)
        
        if args.action == 'list':
            print(json.dumps(db, indent=2))
        elif args.action == 'search' and args.query:
            # Simple search implementation
            print(f"Searching for: {args.query}")
    
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
