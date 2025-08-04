module perceptron (
  input logic signed[7:0] pixel_intensity,
  input logic signed[7:0] weight,
  input logic signed[7:0] bias,
  output logic result
);

  logic signed[7:0] weighted_sum;

  assign weighted_sum = (weight * pixel_intensity) + bias;
  assign result = (weighted_sum > 0) ? 1 : 0;
  
endmodule
