import os
end_prism = "c:/Program Files/prism-4.8.1/bin"

prism_file = """
dtmc

module die

	// local state
	s : [0..7] init 0;
	// value of the die
	d : [0..6] init 0;
	
	[] s=0 -> 0.5 : (s'=1) + 0.5 : (s'=2);
	[] s=1 -> 0.5 : (s'=3) + 0.5 : (s'=4);
	[] s=2 -> 0.5 : (s'=5) + 0.5 : (s'=6);
	[] s=3 -> 0.5 : (s'=1) + 0.5 : (s'=7) & (d'=1);
	[] s=4 -> 0.5 : (s'=7) & (d'=2) + 0.5 : (s'=7) & (d'=3);
	[] s=5 -> 0.5 : (s'=7) & (d'=4) + 0.5 : (s'=7) & (d'=5);
	[] s=6 -> 0.5 : (s'=2) + 0.5 : (s'=7) & (d'=6);
	[] s=7 -> (s'=7);
	
endmodule


"""

properties_file = """
const int x;

P=? [ F s=7 & d=x ]
"""

file = open("C:/prismtest/prism.pm", "w")
file.write(prism_file)
file.close()

file = open("C:/prismtest/properties.pctl", "w")
file.write(properties_file)
file.close()

child =os.chdir(end_prism)
returned_value = os.popen("prism C:/prismtest/prism.pm C:/prismtest/properties.pctl -sim -const x=1").read()

print(returned_value)
