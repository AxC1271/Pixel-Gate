# VGA Controller

## Overview

## Theory and Implementation

```SystemVerilog
-- this is the vga driver for the image processor
module vga_controller (
  input logic clk,
  input logic rst,
  input logic perceptron_output,
  output logic[3:0] red,
  output logic[3:0] green,
  output logic[3:0] blue
);

endmodule
```

## Video Demo

---
