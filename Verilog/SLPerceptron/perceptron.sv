module perceptron (
  input logic signed[7:0] input1,
  input logic signed[7:0] input2,
  input logic signed[7:0] weight1,
  input logic signed[7:0] weight2,
  input logic signed[7:0] bias,
  output logic result
);

  logic signed[7:0] weighted_sum;

  assign weighted_sum = (input1 * weight1) + (input2 * weight2) + bias;
  assign result = (weighted_sum > 0) ? 1 : 0;
  
endmodule
