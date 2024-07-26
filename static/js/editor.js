var editormodel = ace.edit("editor");
editormodel.setTheme("ace/theme/dracula");
editormodel.session.setMode("ace/mode/perl");
editormodel.setOption("showPrintMargin", false);

var editorprop = ace.edit("editor2");
editorprop.setTheme("ace/theme/dracula");
editorprop.session.setMode("ace/mode/properties");
editorprop.setOption("showPrintMargin", false);

var editorterminal = ace.edit("editor3")
editorterminal.setTheme("ace/theme/terminal");
editorterminal.session.setMode("ace/mode/text");
editorterminal.setOption("showPrintMargin", false);
editorterminal.setOption("showLineNumbers", false);
editorterminal.setOption("highlightActiveLine", false)
editorterminal.setOption("showGutter", false);
editorterminal.setReadOnly(true);
