`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 07.08.2023 22:16:15
// Design Name: 
// Module Name: pp_gen
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module pp_gen#(parameter Bitwidth=8)(
	input [Bitwidth-1:0]x,
	input [Bitwidth-1:0]y,
	output pp[Bitwidth-1:0][2*Bitwidth-1:0] ); 	//portlist can be 2D array in verilog 
	
//	wire [2*Bitwidth-1:0]pp_tmp[Bitwidth-1:0];
	wire [Bitwidth-1:0]tmp;
//	wire [2*Bitwidth-1:0]tmp_ans;
	assign tmp=~x+1;
	
	genvar i,j;
	generate
		for(i = 0; i < Bitwidth; i = i +1) begin
		  for(j = 0; j < 2*Bitwidth; j = j +1) begin
		      if(i>j)
                  begin
                      assign pp[i][j]=0;
//                      assign pp_tmp[i][j]=0;
                  end
              else if(j>=Bitwidth+i)
                  begin
                      assign pp[i][j]=pp[i][j-1];
//                      assign pp_tmp[i][j]=pp_tmp[i][j-1];
                  end
              else if(i==Bitwidth-1)
                  begin
                    assign pp[i][j]=tmp[j-i] & y[i];
//                    assign pp_tmp[i][j]=tmp[j-i] & y[i];
                  end
		      else 
                  begin
                     assign pp[i][j] = x[j-i] & y[i] ;
//                     assign pp_tmp[i][j] = x[j-i] & y[i] ;
                  end
		  end
		end
	endgenerate
	
	
//assign tmp_ans=pp_tmp[0]+pp_tmp[1]+pp_tmp[2]+pp_tmp[3]+pp_tmp[4]+pp_tmp[5]+pp_tmp[6]+pp_tmp[7];
	
endmodule
