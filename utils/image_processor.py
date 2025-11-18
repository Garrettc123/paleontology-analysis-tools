#!/usr/bin/env python3
"""Image processing utilities for fossil analysis"""

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from typing import Tuple


class ImageProcessor:
    @staticmethod
    def enhance_image(img: Image.Image) -> Image.Image:
        """Enhance image for better analysis"""
        # Increase contrast
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.5)
        
        # Sharpen
        img = img.filter(ImageFilter.SHARPEN)
        
        return img
    
    @staticmethod
    def detect_edges(img_array: np.ndarray) -> np.ndarray:
        """Detect edges in image"""
        gray = np.mean(img_array, axis=2) if len(img_array.shape) == 3 else img_array
        
        # Sobel edge detection
        gx = np.diff(gray, axis=1)
        gy = np.diff(gray, axis=0)
        
        return np.sqrt(gx[:-1, :]**2 + gy[:, :-1]**2)
    
    @staticmethod
    def calculate_histogram(img_array: np.ndarray) -> Dict:
        """Calculate color histogram"""
        if len(img_array.shape) == 3:
            r_hist = np.histogram(img_array[:,:,0], bins=256)[0]
            g_hist = np.histogram(img_array[:,:,1], bins=256)[0]
            b_hist = np.histogram(img_array[:,:,2], bins=256)[0]
            return {'r': r_hist.tolist(), 'g': g_hist.tolist(), 'b': b_hist.tolist()}
        else:
            hist = np.histogram(img_array, bins=256)[0]
            return {'gray': hist.tolist()}
