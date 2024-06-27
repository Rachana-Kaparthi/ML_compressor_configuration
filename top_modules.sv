`timescale 1ns / 1ps
//`include "pp_reduction_rachana1.sv"
`include "pp_reduction_comp_42.sv"
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 09.08.2023 14:11:03
// Design Name: 
// Module Name: top_modules
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


module top_exact#(parameter Bitwidth=8)(
    input [Bitwidth-1:0]x,y,
    output [2*Bitwidth-1:0]res
    );
    
    wire pp[Bitwidth-1:0][2*Bitwidth-1:0];
    wire [2*Bitwidth-1:0]pp1,pp2;
    
    pp_gen#(.Bitwidth(Bitwidth)) uut(x,y,pp);
    pp_reduction_exact#(.Bitwidth(Bitwidth)) uut1(pp,pp1,pp2);

    assign res=pp1+(pp2<<1);
    
endmodule


//module top_approx1#(parameter Bitwidth=8)(
//    input [Bitwidth-1:0]x,y,
//    output [2*Bitwidth-1:0]res
//    );
    
//    wire pp[Bitwidth-1:0][2*Bitwidth-1:0];
//    wire [2*Bitwidth-1:0]pp1,pp2;
    
//    pp_gen#(.Bitwidth(Bitwidth)) uut(x,y,pp);
//    pp_reduction_approx1#(.Bitwidth(Bitwidth)) uut1(pp,pp1,pp2);

//    assign res=pp1+(pp2<<1);
    
//endmodule

module top_approx2#(parameter Bitwidth=8)(
    input [Bitwidth-1:0]x,y,
    output [2*Bitwidth-1:0]res
    );
    
    wire pp[Bitwidth-1:0][2*Bitwidth-1:0];
    wire [2*Bitwidth-1:0]pp1,pp2;
    
    pp_gen#(.Bitwidth(Bitwidth)) uut(x,y,pp);
    pp_reduction_approx2#(.Bitwidth(Bitwidth)) uut1(pp,pp1,pp2);

    assign res=pp1+(pp2<<1);
    
endmodule


