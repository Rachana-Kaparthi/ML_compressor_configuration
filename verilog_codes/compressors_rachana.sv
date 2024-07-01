`timescale 1ns / 1ps
module FA(input [2:0]p, output [2:1]w   );  // w[2] = carry ;  w[1] =sum
   xor sum(w[1], p[2],p[1],p[0]);   // w1 is sum
   wire ab,bc,ca;
   and a1(ab,p[2],p[1]);
   and a2(bc,p[1],p[0]);
   and a3(ca,p[0],p[2]);
   or carry(w[2], ab,bc,ca);        //w2 is carry
endmodule

module HA(input [1:0]p, output [2:1]w);
    xor sum(w[1],p[0],p[1]);
    and carry(w[2],p[0],p[1]);
endmodule

module exact_compressor_4_2(
    input [3:0]p,
    input cin,
    output sum, 
    output carry,
    output cout);
    wire w1;
    
    FA fa1 (.p(p[3:1])       ,.w({cout,w1}));   //[1](w1),.w[2](cout));
    FA fa2 (.p({p[0],w1,cin}),.w({carry,sum})); //[1](sum),.w[2](carry));
endmodule

module exact_compressor_5_2(
    input [4:0]p,
    input cin1,
    input cin2,
    output sum, 
    output carry,
    output cout1,
    output cout2);
    wire s1,s2;
    
    FA fa1 (.p(p[4:2]),         .w({cout1,s1}) );
    FA fa2 (.p({p[1],s1,cin1}), .w({cout2,s2}) );
    FA fa3 (.p({p[0],s2,cin2}), .w({carry,sum}) );
        
endmodule

module Pos1_Compressor_5_2(sum,carry,a,b,c,d,e);
    input a,b,c,d,e;
    output sum,carry;
    wire w1,w2,w3,t1,t2,t3,t4;
    // sum = a ^ b ^ c ^ d ^ e
    xor u1(sum,a,b,c,d,e);
    // carry = (a & b) | (c & (a ^ b)) | (d & (a | b)) | (e & (a | b | c))
    and u2(t1,a,b);  //(a&b)
    xor u3(w1,a,b);  //(a^b)
    and u4(t2,w1,c); // (c & (a ^ b)) 
    or u5(w2,a,b);   //(a | b)
    and u6(t3,w2,d); //(d & (a | b))
    or u7(w3,a,b,c); //(a | b | c)
    and u8(t4,w3,e); //(e & (a | b | c))
    or u9(carry,t1,t2,t3,t4);


endmodule

// sum_out = a ^ b ^ c ^ d ^ e
//    carry_out = (a & b) | (c & (a ^ b)) | (d & (c ^ (a & b))) | (e & (c ^ (a & b)) & (d ^ (c & (a ^ b))))
   
module Pos2_Compressor_5_2(sum,carry,a,b,c,d,e);
    input a,b,c,d,e;
    output sum,carry;
    wire w1,w2,w3,t1,t2,t3,t4;
    // sum = a ^ b ^ c ^ d ^ e
    xor u1(sum,a,b,c,d,e);
    // carry = (a & b) | (c & (a ^ b)) | (d & (c ^ (a & b))) | (e & (c ^ (a & b)) & (d ^ (c & (a ^ b))))
    and u2(t1,a,b);  //(a&b)
    xor u3(w1,a,b);  //(a^b)
    and u4(t2,w1,c); // (c & (a ^ b)) 
    xor u5(w2,c,t1);   //(c ^ (a & b))
    and u6(t3,w2,d); //(d & (c ^ (a & b)))
    xor u7(w3,c, t1); //(c ^ (a & b)
    and u8(t4,w3,e); //(e & (c ^ (a & b))
    xor u9(w4,t2,d); // (d ^ (c & (a ^ b)))
    and u10(t5,e,w2,w4); // (e & (c ^ (a & b)) & (d ^ (c & (a ^ b))))
    or u11(carry,t1,t2,t3,t5);


endmodule

module Pos3_Compressor_5_2(sum,carry,a,b,c,d,e);
    input a,b,c,d,e;
    output sum,carry;
    wire w1,w2,w3,t1,t2,t3;
    /////   sum = a+b+c+d+e /////
    or u1 (sum,a,b,c,d,e);
    /////   carry = a(b+c+d+e) + (b+c)(d+e) + de     /////
    or u2 (w1,b,c,d,e);     //(b+c+d+e)
    and u3 (t1,a,w1);       //a(b+c+d+e)
    or u4 (w2,d,e);         //(d + e)
    or u5 (w3,b,c);         //(b + c)
    and u6 (t2,w2,w3);      //(b+c)(d+e)
    and u7 (t3,d,e);        //de
    or u8 (carry,t1,t2,t3);
endmodule

module Pos4_Compressor_5_2(sum,carry,a,b,c,d,e);
    input a,b,c,d,e;
    output sum,carry;
    wire w1,w2,w3,t1,t2,t3;
    /////   sum = a+b+c+d+e /////
    or u1 (sum,a,b,c,d,e);
    /////   carry = a(b+c+d+e) + bc(d + e) + de(b + c)
    or u2 (w1,b,c,d,e);     //(b+c+d+e)
    and u3 (t1,a,w1);       //a(b+c+d+e)
    or u4 (w2,d,e);         //(d + e)
    and u5 (t2,b,c,w2);     //bc(d + e)
    or u6 (w3,b,c);         //(b + c)
    and u7 (t3,d,e,w3);     //de(b + c)
    or u8 (carry,t1,t2,t3);
endmodule



//brent
module Pos5_Compressor_5_2(sum,carry,a,b,c,d,e);
    input a,b,c,d,e;
    output sum,carry;
    wire w1,w2,w3,w4,t1,t2,t3,t4,v1,v2,v3;
// sum sum_out = a ^ b ^ c ^ d ^ e
    xor u1(sum,a,b,c,d,e);
    // Carry  (p1 | (p2 & g1)) | (e & (g1 | (p2 & g2)))
//    p1 = a & b
//    p2 = c & d
//    g1 = a | b
//    g2 = c | d
    and u2(t1,a,b);
    and u3(w1,c,d);
    or u4(w2,a,b);
    and u5(t2,w1,w2);
    and u6(t3,e,w2);
    or u7(w3,c,d);
    and u8(t4,w1,w3);
    or u9(carry,t1,t2,t3,t4);

endmodule


module Pos1_Compressor_4_2(sum,carry,a,b,c,d);
    input a,b,c,d;
    output sum,carry;
    wire w1,w2,t1,t2,t3,v1,v2;
    //// sum_out = a ^ b ^ c ^ d
    xor u1 (sum,a,b,c,d);
    //// carry_out = (a & b) | (c & (a ^ b) ) 
    and u2 (t1,a,b);
    xor u3 (w1,a,b);
    and u4 (t2,c,w1);
    or u5 (carry,t1,t2);
endmodule

//     sum =((a^b)&(c&d))|((~(a^b))&(c|d))
    // carry = a|b
module Pos2_Compressor_4_2(sum,carry,a,b,c,d);
    input a,b,c,d;
    output sum,carry;
    wire w1,w2,w3,w4,t1,t2;
    //// sum =((a^b)&(c&d))|((~(a^b))&(c|d))
    xor u1 (w1,a,b); //(a^b)
    and u2 (w2,c,d); //(c&d)
    and u3 (t1,w1,w2);// ((a^b)&(c&d))
    not u4 (w3,w1); //(~(a^b))
    or u5 (w4,c,d); //(c|d)
    and u6 (t2,w3,w4); // ((~(a^b))&(c|d))
    or u7 (sum,t1,t2); //((a^b)&(c&d))|((~(a^b))&(c|d))
    //// carry = a|b
    or u8 (carry,a,b);
endmodule
//     sum = a|b|c|d
    // carry = (a&b)|(b&c)|(d&b)|(c&d)
    
module Pos3_Compressor_4_2(sum,carry,a,b,c,d);
    input a,b,c,d;
    output sum,carry;
    wire w1,w2,t1,t2;
    /////    sum = a|b|c|d   /////
    or u1 (sum,a,b,c,d);
    /////   carry = ab+cd+bc+bd   /////
    and u2 (w1,a,b);
    and u3 (w2,c,d);
    and u4 (t1,b,c):
    and u5 (t2,b,d):
    or u6 (carry,t1,t2,w1,w2);
endmodule

module Pos4_Compressor_4_2(sum,carry,a,b,c,d);
    input a,b,c,d;
    output sum,carry;
    wire w1,w2,t1,t2;
    /////   sum = a+b+c+d   /////
    or u1 (sum,a,b,c,d);
    /////   carry = ab+cd   /////
    and u2 (t1,a,b);
    and u3 (t2,c,d);
    or u4 (carry,t1,t2);
endmodule

module Pos5_Compressor_4_2(sum,carry,a,b,c,d);
    input a,b,c,d;
    output sum,carry;
    wire w1,w2,t1,t2,t3,v1,v2;
    //// sum =((a^b^c^d)|(a & b & c ))
    xor u1 (w1,a,b,c,d);
    and u2 (w2,a,b,c);
    or u9 (sum,w1,w2);
    //// carry = ((a&(b|c|d))|(b&(c|d))|(c&d))
    or u3 (v1,b,c,d);
    and u4 (t1,a,v1); //(a&(b|c|d))
    or u5 (v2,c,d);
    and u6 (t2,b,v2); //(b&(c|d))
    and u7 (t3,c,d);  //(c&d)
    or u8 (carry,t1,t2,t3);
endmodule

module Pos6_Compressor_4_2(a,b,c,d,sum,carry);
 output sum,carry;
 input a,b,c,d;
 wire t1,t2;

 assign t1 = a^b;
 assign t2 = c^d;
 assign sum = ((~t1)&(t2) | ((t1)&(~t2)) | (a&b&c&d));
 assign carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))));

endmodule

module Pos7_Compressor_4_2(a,b,c,d,sum,carry);
 output sum,carry;
 input a,b,c,d;
 wire t1,t2;

 assign t1 = a^b;
 assign t2 = c^d;
 assign sum = (((~t1)&(t2)) | ((t1)&(~t2)));
 assign carry = ~((~(a|b)&(~(c&d))) | (~(c|d)&(~(a&b))));

endmodule

module Pos8_Compressor_4_2(a,b,c,d,sum,carry);
 output sum,carry;
 input a,b,c,d;
 wire t1,t2;

 assign t1 = a^b;
 assign t2 = c^d;
 assign sum = (((~t1)&(c|d)) | ((t1)&(~t2)));
 assign carry = ~(((~(a|b))&(~(c&d))) | ((~(c|d))&(~(a&b))));

endmodule

module Pos9_Compressor_4_2(sum,carry,a,b,c,d);
 output sum,carry;
 input a,b,c,d;
 wire d1,d2,d3,d4,O2,O3,O4;

assign carry = ~O3;                   
assign sum = (O3&(~O4)) | (~O2);
assign d1 = ~(a|b);
assign d2 = ~(c|d);
assign d3 = ~(a&b);
assign d4 = ~(c&d);
assign O4 = d1 & d2;
assign O3 = (d1 | d2) & (d3 & d4);
assign O2 = (d1 | d2) | (d3 & d4);

endmodule

//module Pos10_Compressor_5_2(sum,carry,a,b,c,d,e);
//    input a,b,c,d,e;
//    output sum,carry;
//    wire w1,w2,w3,w4,t1,t2,t3,t4,v1,v2,v3;

//    // sum = ((a ^ b ^ c ^ d ^ e)|(a & (b|c) & (e|d)))
//    xor u1(w1,a,b,c,d,e);
//    or u2(w2,b,c);
//    or u3(w3,d,e);
//    and u4(w4,a,w2,w3);
//    or u6(sum,w1,w4);

//    //  carry = (a & (b|c|d|e)) | (b&(c|d|e)) | (c&(d|e)) | (d&e))

//    or u7(v1,c,b,d,e);   // (b|c|d|e)
//    and u8(t1,v1,a);     // (a & (b|c|d|e)) 
//    or u9(v2,c,d,e);     // (c|d|e)
//    and u10(t2,v2,b);    // (b&(c|d|e))
//    or u11(v3,d,e);      //(d|e)
//    and u12(t3,v3,c);    //(c&(d|e))
//    and u13(t4,d,e);     //(d&e)
//    or u14(carry,t1,t2,t3,t4);

//endmodule

 
    