`timescale 1ns / 1ps
// ************** Single Row Reduction module Exact ***************//
//***************************Edit the compressor position numbers according to the required configuration *************************//
module single_row_reduction_firststage_exact#(parameter Bitwidth=8)(

    input [Bitwidth-1:0]pp_row,
    input cin1,cin2,
    output [Bitwidth/2-1:0]pp_second_stage,
    output cout1,cout2
    );

exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));

endmodule

// ************** single row reduction module for p7*****************//
module single_row_reduction_firststage_p7#(parameter Bitwidth=8)(

    input [Bitwidth-1:0]pp_row,
//    input cin1,cin2,
    output [Bitwidth/2-1:0]pp_second_stage
//    output cout1,cout2
    );
Pos4_Compressor_4_2 pos42_0(.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.a(pp_row[7]),.b(pp_row[6]),.c(pp_row[5]),.d(pp_row[4]));
//exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
Pos4_Compressor_4_2 pos42_1(.sum(pp_second_stage[0]),.carry(pp_second_stage[1]),.a(pp_row[3]),.b(pp_row[2]),.c(pp_row[1]),.d(pp_row[0]));

endmodule

// ************** single row reduction module for p6*****************//
module single_row_reduction_firststage_p6#(parameter Bitwidth=8)(

    input [Bitwidth-1:0]pp_row,
//    input cin1,cin2,
    output [Bitwidth/2-1:0]pp_second_stage
//    output cout1,cout2
    );
Pos9_Compressor_4_2 pos42(.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.a(pp_row[7]),.b(pp_row[6]),.c(pp_row[5]),.d(pp_row[4]));
//exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
FA exact32(.p(pp_row[3:1]),.w(pp_second_stage[1:0]));


endmodule


// ************** single row reduction module for p5*****************//
module single_row_reduction_firststage_p5#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
Pos7_Compressor_4_2 pos42(.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.a(pp_row[7]),.b(pp_row[6]),.c(pp_row[5]),.d(pp_row[4]));
//exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
HA exact32(.p(pp_row[3:2]),.w(pp_second_stage[1:0]));


endmodule

// ************** single row reduction module for p4*****************//
module single_row_reduction_firststage_p4#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
Pos9_Compressor_4_2 pos42(.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.a(pp_row[7]),.b(pp_row[6]),.c(pp_row[5]),.d(pp_row[4]));
//exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
// FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));
assign pp_second_stage[0] = pp_row[3];
assign pp_second_stage[1] = 2'b0;
//pp_second_stage[1] = 1'b0;


endmodule

// ************** single row reduction module for p3*****************//
module single_row_reduction_firststage_p3#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
Pos6_Compressor_4_2 pos42(.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.a(pp_row[7]),.b(pp_row[6]),.c(pp_row[5]),.d(pp_row[4]));
//exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
// FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));

assign pp_second_stage[1:0] = 2'b0;
//pp_second_stage[1] = 1'b0;


endmodule

// ************** single row reduction module for p2*****************//
module single_row_reduction_firststage_p2#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
FA firststage (.p(pp_row[7:5]),.w({pp_second_stage[2],pp_second_stage[3]}));
// FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));

assign pp_second_stage[1:0] = 2'b0;
//pp_second_stage[1] = 1'b0;


endmodule

// ************** single row reduction module for p1*****************//
module single_row_reduction_firststage_p1#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
HA firststage (.p(pp_row[7:6]),.w({pp_second_stage[2],pp_second_stage[3]}));
// FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));

assign pp_second_stage[1:0] = 2'b0;
//pp_second_stage[1] = 1'b0;


endmodule


// ************** single row reduction module for p0*****************//
module single_row_reduction_firststage_p0#(parameter Bitwidth=8)(

    input logic [Bitwidth-1:0] pp_row,
//    input cin1,cin2,
    output logic [Bitwidth/2-1:0] pp_second_stage
//    output cout1,cout2
    );
//HA firststage (.p(pp_row[0:1]),.w(pp_second_stage[3:2]));
// FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));

assign pp_second_stage[2:0] = 3'b0;
assign pp_second_stage[3] = pp_row[7];


endmodule

//******************* Reduction Module Exact ********************//

module pp_reduction_exact#(parameter Bitwidth=8)(

    input pp[Bitwidth-1:0][2*Bitwidth-1:0],
    output [2*Bitwidth-1:0]pp1,pp2
    );
    
    wire [2*Bitwidth:0]cin1,cin2;
    wire [2*Bitwidth-1:0]pp_1st_stage_op[Bitwidth/2-1:0];
    
    assign cin1[0]=0;
    assign cin2[0]=0;
    
    //************ First Stage **************//
     
    genvar i;
    
    generate
        for(i=0;i<2*Bitwidth;i++) begin
            if(i>=Bitwidth) begin
             single_row_reduction_firststage_exact#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]}),.cin1(cin1[i]),.cin2(cin2[i]),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}),.cout1(cin1[i+1]),.cout2(cin2[i+1]));
            end
            else if(i == 0)
                begin
                    assign pp_1st_stage_op[0][i] = pp[0][i];
                    assign pp_1st_stage_op[1][i] = 2'b0;
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;

                end
            else if(i == 1)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));
                    HA exact32_HA(.p({pp[0][i],pp[1][i]}),.w({pp_1st_stage_op[1][i],pp_1st_stage_op[0][i]}));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if(i == 2)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));
                    FA exact32_FA(.p({pp[0][i],pp[1][i],pp[2][i]}),.w({pp_1st_stage_op[1][i],pp_1st_stage_op[0][i]}));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if(i == 3)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));

                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(0),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if( i==4 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    //exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));
                    assign pp_1st_stage_op[3][i] = pp[4][i];
                    assign pp_1st_stage_op[2][i] = 2'b0;
                end
            else if( i==5 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    HA exact32(.p({pp[5][i],pp[6][i]}),.w({pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));

                end  
            else if( i==6 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    FA exact32(.p({pp[5][i],pp[6][i],pp[7][i]}),.w({pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));

                end  
            else if( i==7 )
                begin
                    exact_compressor_4_2 exact42_1(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    exact_compressor_4_2 exact42_2(.p({pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.cin(0),.sum(pp_1st_stage_op[3][i]),.carry(pp_1st_stage_op[2][i]),.cout(cin2[i+1]));

                end             
        end
    endgenerate
    
    //************ Second Stage **************//
    wire [2*Bitwidth-1:0]pp_2nd_stage_ip[Bitwidth/2-1:0];
    wire [2*Bitwidth:0]cin21;
    
    assign pp_2nd_stage_ip[Bitwidth/2-1]=pp_1st_stage_op[Bitwidth/2-1];
    assign pp_2nd_stage_ip[Bitwidth/2-2]=pp_1st_stage_op[Bitwidth/2-2]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-3]=pp_1st_stage_op[Bitwidth/2-3]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-4]=pp_1st_stage_op[Bitwidth/2-4];
    assign cin21[0]=0;
   // assign pp2[0]=0;
    
    genvar j;
    
    generate
        for(j=0;j<2*Bitwidth;j++) begin
             exact_compressor_4_2 secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j],pp_2nd_stage_ip[2][j],pp_2nd_stage_ip[3][j]}),.cin(cin21[j]),.sum(pp1[j]),.carry(pp2[j]),.cout(cin21[j+1]));
        end
    endgenerate
    
//    wire [2*Bitwidth-1:0]res;
//    assign res=pp1+(pp2<<1);
endmodule

// **************pp_reduction_approx for positions**************//

module pp_reduction_approx2#(parameter Bitwidth=8)(

    input  pp[Bitwidth-1:0][2*Bitwidth-1:0],
    output [2*Bitwidth-1:0] pp1,pp2
    );
    
    wire [2*Bitwidth:0]cin1,cin2;
    wire [2*Bitwidth-1:0]pp_1st_stage_op[Bitwidth/2-1:0];
    
    assign cin1[Bitwidth:0]=0;
    assign cin2[Bitwidth:0]=0;
   
    //************ First Stage [1,1,1,1,5,1,5,1]**************//
     
    genvar i;
    
    generate
        for(i=0;i<2*Bitwidth;i++) begin
            if (i>=Bitwidth) 
                begin
                    single_row_reduction_firststage_exact#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.cin1(cin1[i]),.cin2(cin2[i]),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}),.cout1(cin1[i+1]),.cout2(cin2[i+1]));
                end
            else if( i==7 )
                begin
                    single_row_reduction_firststage_p7#(.Bitwidth(Bitwidth)) firststage  (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
                end
            else if( i==6 )
                begin
                    single_row_reduction_firststage_p6#(.Bitwidth(Bitwidth)) firststage  (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
                end
            else if( i==5 )
                begin
                    single_row_reduction_firststage_p5#(.Bitwidth(Bitwidth)) firststage  (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
                end
            else if( i==4 )
                begin
//                    Pos1_Compressor_5_2 firststage (.sum(pp_1st_stage_op[3][i]),.carry(pp_1st_stage_op[2][i]),.a(pp[0][i]),.b(pp[1][i]),.c(pp[2][i]),.d(pp[3][i]),.e(pp[4][i]));
//                    assign pp_1st_stage_op[1][i] = 1'b0;
//                    assign pp_1st_stage_op[0][i] = 1'b0;
                    single_row_reduction_firststage_p4#(.Bitwidth(Bitwidth)) firststage  (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
                end
            else if( i==3 )
                begin
//                    Pos1_Compressor_4_2 firststage (.sum(pp_1st_stage_op[3][i]),.carry(pp_1st_stage_op[2][i]),.a(pp[0][i]),.b(pp[1][i]),.c(pp[2][i]),.d(pp[3][i]));
//                    assign pp_1st_stage_op[1][i] = 1'b0;
//                    assign pp_1st_stage_op[0][i] = 1'b0;
                    single_row_reduction_firststage_p3#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
   
                end
            else if( i==2 )
                begin
//                   FA firststage (.p(pp[0:2]),.w(pp_1st_stage_op[3:2]));
//                   assign pp_1st_stage_op[1][i] = 1'b0;
//                   assign pp_1st_stage_op[0][i] = 1'b0;
                   single_row_reduction_firststage_p2#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
   
                end
            else if( i==1 )
                begin
//                    HA firststage (.p(pp[0:1]),.w(pp_1st_stage_op[3:2]));
//                    assign pp_1st_stage_op[1][i] = 1'b0;
//                    assign pp_1st_stage_op[0][i] = 1'b0;
                    single_row_reduction_firststage_p1#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
   
                end
            else if( i==0 )
                begin
//                   assign pp_1st_stage_op[3][i] = pp[0][i];
//                   assign pp_1st_stage_op[2][i] = 1'b0;
//                   assign pp_1st_stage_op[1][i] = 1'b0;
//                   assign pp_1st_stage_op[0][i] = 1'b0;
                    single_row_reduction_firststage_p0#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[0][i],pp[1][i],pp[2][i],pp[3][i],pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));
   
                end
        end
    endgenerate
    
    //************ Second Stage[5,4,1,5,1,5,5,5] **************//
    wire [2*Bitwidth-1:0]pp_2nd_stage_ip[Bitwidth/2-1:0];
    wire [2*Bitwidth:0]cin21;
    
    assign pp_2nd_stage_ip[Bitwidth/2-1]=pp_1st_stage_op[Bitwidth/2-1];
    assign pp_2nd_stage_ip[Bitwidth/2-2]=pp_1st_stage_op[Bitwidth/2-2]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-3]=pp_1st_stage_op[Bitwidth/2-3]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-4]=pp_1st_stage_op[Bitwidth/2-4];
    assign cin21[Bitwidth:0]=0;
   // assign pp2[0]=0;
    
    genvar j;
    
    generate
        for(j=0;j<2*Bitwidth;j++) begin
            exact_compressor_4_2 secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j],pp_2nd_stage_ip[2][j],pp_2nd_stage_ip[3][j]}),.cin(cin21[j]),.sum(pp1[j]),.carry(pp2[j]),.cout(cin21[j+1]));
//             if (j>=(Bitwidth-2)) 
//                 begin
//                     exact_compressor_4_2 secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j],pp_2nd_stage_ip[2][j],pp_2nd_stage_ip[3][j]}),.cin(cin21[j]),.sum(pp1[j]),.carry(pp2[j]),.cout(cin21[j+1]));
//                 end
// //            else if(j==7)
// //                begin
// //                    Pos7_Compressor_4_2 secondstage(.sum(pp1[j]),.carry(pp2[j]),.a(pp_2nd_stage_ip[0][j]),.b(pp_2nd_stage_ip[1][j]),.c(pp_2nd_stage_ip[2][j]),.d(pp_2nd_stage_ip[3][j]));
// //                end   
// //            else if(j==6)
// //                begin
// //                    Pos9_Compressor_4_2 secondstage(.sum(pp1[j]),.carry(pp2[j]),.a(pp_2nd_stage_ip[0][j]),.b(pp_2nd_stage_ip[1][j]),.c(pp_2nd_stage_ip[2][j]),.d(pp_2nd_stage_ip[3][j]));
// //                end 
//             else if(j==5 || j==4)
//                 begin
//                     FA secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j],pp_2nd_stage_ip[3][j]}),.w({pp2[j],pp1[j]}));
//                 end
//             else if( j==3 || j==2)
//                 begin
//                     HA secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j]}),.w({pp2[j],pp1[j]}));
//                 end 
//             else if(j==1|| j==0)
//                 begin
//                     assign pp1[j] = pp_2nd_stage_ip[0][j];
//                     assign pp2[j] = 1'b0;
//                 end 

        end
    endgenerate
    
//    wire [2*Bitwidth-1:0]res;
//    assign res=pp1+(pp2<<1);
endmodule

//******************* Reduction Module Approx Combinations ********************//

module pp_reduction_approx1#(parameter Bitwidth=8)(

    input pp[Bitwidth-1:0][2*Bitwidth-1:0],
    output [2*Bitwidth-1:0]pp1,pp2
    );
    
    wire [2*Bitwidth:0]cin1,cin2;
    wire [2*Bitwidth-1:0]pp_1st_stage_op[Bitwidth/2-1:0];
    
    assign cin1[0]=0;
    assign cin2[0]=0;
    
    //************ First Stage **************//
     
    genvar i;
    
    generate
        for(i=0;i<2*Bitwidth;i++) begin
            if(i>=Bitwidth) begin
             single_row_reduction_firststage_exact#(.Bitwidth(Bitwidth)) firststage (.pp_row({pp[7][i],pp[6][i],pp[5][i],pp[4][i],pp[3][i],pp[2][i],pp[1][i],pp[0][i]}),.cin1(cin1[i]),.cin2(cin2[i]),.pp_second_stage({pp_1st_stage_op[0][i],pp_1st_stage_op[1][i],pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}),.cout1(cin1[i+1]),.cout2(cin2[i+1]));
            end
            else if(i == 0)
                begin
                    assign pp_1st_stage_op[0][i] = pp[0][i];
                    assign pp_1st_stage_op[1][i] = 2'b0;
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;

                end
            else if(i == 1)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));
                    HA exact32_HA(.p({pp[0][i],pp[1][i]}),.w({pp_1st_stage_op[1][i],pp_1st_stage_op[0][i]}));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if(i == 2)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));
                    FA exact32_FA(.p({pp[0][i],pp[1][i],pp[2][i]}),.w({pp_1st_stage_op[1][i],pp_1st_stage_op[0][i]}));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if(i == 3)
                begin

                    // exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[2:0]),.w(pp_second_stage[1:0]));
                    Pos1_Compressor_4_2 pos42(.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.a(pp[0][i]),.b(pp[1][i]),.c(pp[2][i]),.d(pp[3][i]));

                    // exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(0),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    assign pp_1st_stage_op[2][i] = 2'b0;
                    assign pp_1st_stage_op[3][i] = 2'b0;
                end
            else if( i==4 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(0),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    //exact_compressor_5_2 exact52(.p(pp_row[Bitwidth-1:Bitwidth-5]),.cin1(cin1),.cin2(cin2),.sum(pp_second_stage[3]),.carry(pp_second_stage[2]),.cout1(cout1),.cout2(cout2));
                    // FA exact32(.p(pp_row[5:7]),.w(pp_second_stage[1:0]));
                    assign pp_1st_stage_op[3][i] = pp[4][i];
                    assign pp_1st_stage_op[2][i] = 2'b0;
                end
            else if( i==5 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    HA exact32(.p({pp[5][i],pp[6][i]}),.w({pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));

                end  
            else if( i==6 )
                begin
                    exact_compressor_4_2 exact42(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    FA exact32(.p({pp[5][i],pp[6][i],pp[7][i]}),.w({pp_1st_stage_op[2][i],pp_1st_stage_op[3][i]}));

                end  
            else if( i==7 )
                begin
                    exact_compressor_4_2 exact42_1(.p({pp[0][i],pp[1][i],pp[2][i],pp[3][i]}),.cin(cin1[i]),.sum(pp_1st_stage_op[0][i]),.carry(pp_1st_stage_op[1][i]),.cout(cin1[i+1]));
                    exact_compressor_4_2 exact42_2(.p({pp[4][i],pp[5][i],pp[6][i],pp[7][i]}),.cin(0),.sum(pp_1st_stage_op[3][i]),.carry(pp_1st_stage_op[2][i]),.cout(cin2[i+1]));

                end             
        end
    endgenerate
    
    //************ Second Stage **************//
    wire [2*Bitwidth-1:0]pp_2nd_stage_ip[Bitwidth/2-1:0];
    wire [2*Bitwidth:0]cin21;
    
    assign pp_2nd_stage_ip[Bitwidth/2-1]=pp_1st_stage_op[Bitwidth/2-1];
    assign pp_2nd_stage_ip[Bitwidth/2-2]=pp_1st_stage_op[Bitwidth/2-2]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-3]=pp_1st_stage_op[Bitwidth/2-3]<<1;
    assign pp_2nd_stage_ip[Bitwidth/2-4]=pp_1st_stage_op[Bitwidth/2-4];
    assign cin21[0]=0;
   // assign pp2[0]=0;
    
    genvar j;
    
    generate
        for(j=0;j<2*Bitwidth;j++) begin
             exact_compressor_4_2 secondstage(.p({pp_2nd_stage_ip[0][j],pp_2nd_stage_ip[1][j],pp_2nd_stage_ip[2][j],pp_2nd_stage_ip[3][j]}),.cin(cin21[j]),.sum(pp1[j]),.carry(pp2[j]),.cout(cin21[j+1]));
        end
    endgenerate
    
//    wire [2*Bitwidth-1:0]res;
//    assign res=pp1+(pp2<<1);
endmodule
