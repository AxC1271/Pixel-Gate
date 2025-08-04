# 🖼️ Pixel Gate

Welcome to my PixelGate project! This project explores how a single-layer perceptron can be used to perform image thresholding and display the results on a VGA monitor, with the end goal of implementing both a software-based simulation and a hardware-based FPGA implementation.

## 🎯 Project Goals

- Implement a single-layer perceptron to perform image thresholding using fixed-point arithmetic in SystemVerilog.
- Visualize the thresholding process and image transformation.
- Translate the perceptron logic into a hardware-friendly format and implement it in SystemVerilog on an FPGA (e.g., Basys3).
- Build a fully autonomous image processing system that runs independently on FPGA hardware and displays results on a VGA monitor.

## 🧠 Perceptron Overview

This project uses a Single-Layer Perceptron:
- Input representation: Encodes pixel intensity values from a grayscale image.
- Output space: Binary classification of pixels as "on" or "off" based on a threshold.
- Thresholding structure:
  - Weighted sum calculation
  - Step function activation
  - Fixed-point arithmetic for efficient hardware implementation

The training and simulation are done in Python to determine optimal weights and bias. The hardware implementation is done in SystemVerilog.

## 🖥️ Image Processing Environment

The image processing is implemented in SystemVerilog, with the perceptron logic handling pixel classification. The VGA controller interacts with the display environment by:
- Receiving binary pixel data from the perceptron.
- Generating VGA signals to render the thresholded image.
- Displaying the processed image on a VGA monitor.

## Basic Theory

Single layer perceptrons are one of the simplest form of artificial neural networks; they are a type of linear classifiers used for supervised learning and can decide whether an input, represented by some arbitary vector, belongs to a specific class. The perceptron consists of a bunch of nodes, which each node has their own associated weight that determines the overall significance of the input. The sum of these node's outputs are then passed to an activation function, which is traditionally a Heaviside step function to produce a binary output.

Image thresholding is a technique used to convert grayscale images into binary images by classifying pixels based on intensity. The primary objective is to separate foreground from background, enhancing features for further analysis or display. Unlike complex neural networks, a single-layer perceptron uses a simple linear function to make binary decisions.
Key components of image thresholding include:
- Perceptron: The decision-maker that processes pixel intensity values.
- Input: Grayscale pixel values from the image.
- Output: Binary classification of pixels as "on" or "off".
- Weighted Sum: Calculation of the weighted sum of pixel intensity and bias.
- Activation Function: A step function that determines the binary output based on the weighted sum.
- VGA Display: The system that renders the binary image on a monitor.

The end result is that the grayscale image gets converted into a binary image with each individual pixel being set to either black or white based on some specific threshold value. The primary goal of thresholding is to simplify the image, making it easier to identify and analyze regions of interest.

---

This README is just a summary of the project at a high level, please go into both the `Python` and `SystemVerilog` submodules to read more in depth about the lower level implementation.

