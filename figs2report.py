import glob

# Set folder path where figures are
folder_path = "test_figs"

# Set report title to appear on first page
report_title = "Important Report"
authors = "Authors"

# Get full path of all files with extension: fig_ext
fig_ext = ".png"
fig_files = glob.glob(folder_path+"/*"+fig_ext)

# Sort alphabetically
fig_files.sort()

# Create simple latex file (.tex) with one fig per page
with open('report.tex', 'w') as f:
    # Header of text document goes here
    f.write("\documentclass{article} \n")
    f.write("\\usepackage{graphicx} \n \n")
    f.write("\\title{"+report_title+"} \n")
    f.write("\\author{"+authors+"} \n")
    f.write("\date{\\today} \n \n")
    f.write("\\begin{document} \n \n")
    f.write("\maketitle \n")
    f.write("\\newpage \n")

    # Loop over all figure files and write to tex-file
    for fig in fig_files:
        f.write('\n')
        f.write("\includegraphics[width=1.0\\textwidth]{"+fig+"}")
        f.write("\n \\newpage")
        f.write('\n')

    # End of text document goes here
    f.write("\n")
    f.write("\end{document}")
