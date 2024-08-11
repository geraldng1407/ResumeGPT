def get_modules():
    return r"""
\documentclass[10pt, a4paper]{article}
% Packages:
\usepackage[
    ignoreheadfoot, % set margins without considering header and footer
    top=0.5 cm, % seperation between body and page edge from the top
    bottom=1 cm, % seperation between body and page edge from the bottom
    left=1 cm, % seperation between body and page edge from the left
    right=1 cm, % seperation between body and page edge from the right
    footskip=1.0 cm, % seperation between body and footer
    % showframe % for debugging 
]{geometry} % for adjusting page geometry
\usepackage{titlesec} % for customizing section titles
\usepackage{tabularx} % for making tables with fixed width columns
\usepackage{array} % tabularx requires this
\usepackage[dvipsnames]{xcolor} % for coloring text
\definecolor{primaryColor}{RGB}{0, 0, 0} % define primary color
\usepackage{enumitem} % for customizing lists
\usepackage{fontawesome5} % for using icons
\usepackage{amsmath} % for math
\usepackage[
    pdftitle={Ng Zhi Hui Gerald Resume},
    pdfauthor={Gerald},
    pdfcreator={LaTeX with RenderCV},
    colorlinks=true,
    urlcolor=primaryColor
]{hyperref} % for links, metadata and bookmarks
\usepackage[pscoord]{eso-pic} % for floating text on the page
\usepackage{calc} % for calculating lengths
\usepackage{bookmark} % for bookmarks
\usepackage{lastpage} % for getting the total number of pages
\usepackage{changepage} % for one column entries (adjustwidth environment)
\usepackage{paracol} % for two and three column entries
\usepackage{ifthen} % for conditional statements
\usepackage{needspace} % for avoiding page brake right after the section title
\usepackage{iftex} % check if engine is pdflatex, xetex or luatex

% Ensure that generate pdf is machine readable/ATS parsable:
\ifPDFTeX
    \input{glyphtounicode}
    \pdfgentounicode=1
    \usepackage[T1]{fontenc}
    \usepackage[utf8]{inputenc}
    \usepackage{lmodern}
\fi

\usepackage{charter}

% Some settings:
\raggedright
\AtBeginEnvironment{adjustwidth}{\partopsep0pt} % remove space before adjustwidth environment
\pagestyle{empty} % no header or footer
\setcounter{secnumdepth}{0} % no section numbering
\setlength{\parindent}{0pt} % no indentation
\setlength{\topskip}{0pt} % no top skip
\setlength{\columnsep}{0.15cm} % set column seperation
\pagenumbering{gobble} % no page numbering

\titleformat{\section}{\needspace{4\baselineskip}\bfseries\large}{}{0pt}{}[\vspace{1pt}\titlerule]

\titlespacing{\section}{
    % left space:
    -1pt
}{
    % top space:
    0.3 cm
}{
    % bottom space:
    0.2 cm
} % section title spacing

\renewcommand\labelitemi{$\vcenter{\hbox{\small$\bullet$}}$} % custom bullet points
\newenvironment{highlights}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=0 cm + 10pt
    ]
}{
    \end{itemize}
} % new environment for highlights


\newenvironment{highlightsforbulletentries}{
    \begin{itemize}[
        topsep=0.10 cm,
        parsep=0.10 cm,
        partopsep=0pt,
        itemsep=0pt,
        leftmargin=10pt
    ]
}{
    \end{itemize}
} % new environment for highlights for bullet entries

\newenvironment{onecolentry}{
    \begin{adjustwidth}{
        0 cm + 0.00001 cm
    }{
        0 cm + 0.00001 cm
    }
}{
    \end{adjustwidth}
} % new environment for one column entries

\newenvironment{twocolentry}[2][]{
    \onecolentry
    \def\secondColumn{#2}
    \setcolumnwidth{\fill, 6.5 cm}
    \begin{paracol}{2}
}{
    \switchcolumn \raggedleft \secondColumn
    \end{paracol}
    \endonecolentry
} % new environment for two column entries

\newenvironment{threecolentry}[3][]{
    \onecolentry
    \def\thirdColumn{#3}
    \setcolumnwidth{, \fill, 4.5 cm}
    \begin{paracol}{3}
    {\raggedright #2} \switchcolumn
}{
    \switchcolumn \raggedleft \thirdColumn
    \end{paracol}
    \endonecolentry
} % new environment for three column entries

% \newenvironment{header}{
%     \setlength{\topsep}{0pt}\par\kern\topsep\centering\linespread{1.5}
% }{
%     \par\kern\topsep
% } % new environment for the header
\newenvironment{header}{
    \setlength{\topsep}{0pt}\par\kern0pt\centering\linespread{1.5}
}{
    \par\kern\topsep
}

\newcommand{\placelastupdatedtext}{% \placetextbox{<horizontal pos>}{<vertical pos>}{<stuff>}
  \AddToShipoutPictureFG*{% Add <stuff> to current page foreground
    \put(
        \LenToUnit{\paperwidth-2 cm-0 cm+0.05cm},
        \LenToUnit{\paperheight-1.0 cm}
    ){\vtop{{\null}\makebox[0pt][c]{
        \small\color{gray}\textit{Last updated in July 2024}\hspace{\widthof{Last updated in July 2024}}
    }}}%
  }%
}%

% save the original href command in a new command:
\let\hrefWithoutArrow\href
\begin{document}
    \newcommand{\AND}{\unskip
        \cleaders\copy\ANDbox\hskip\wd\ANDbox
        \ignorespaces
    }
    \newsavebox\ANDbox
    \sbox\ANDbox{$|$}
"""

def get_header():
    return r"""
\begin{header}
    \fontsize{20 pt}{20 pt}\selectfont Ng Zhi Hui Gerald

    \vspace{5 pt} % Adjust this spacing as needed

    \small % Reduce font size for contact information
    \makebox[\textwidth][c]{
        \faIcon{envelope}
        \hrefWithoutArrow{mailto:gerald.ng@outlook.sg}{gerald.ng@outlook.sg} \ | \
        \faIcon{phone}
        +65 98584816 \ | \
        \faIcon{globe}
        \hrefWithoutArrow{https://geraldng.vercel.app/}{geraldng.vercel.app/} \ | \
        \faIcon{linkedin}
        \hrefWithoutArrow{https://www.linkedin.com/in/nggerald}{linkedin.com/in/nggerald} \ | \
        \faIcon{github}
        \hrefWithoutArrow{https://github.com/geraldng1407}{github.com/geraldng1407}
    }
\end{header}
\vspace{-0.5 cm}

"""

def get_education():
    return r"""
    \section{Education}
        \begin{twocolentry}{
            Aug 2021 – Dec 2024 (expected)
        }
            \textbf{Singapore Management University}, \end{twocolentry}
        \textit{Degree in Bachelor of Science (Computer Science)}
        % \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
                \item Cumulative GPA: 3.54/4.0 (Cum Laude)  
                \item  Artificial Intelligence and Cybersecurity with a Second Major in Business Analytic
            \end{highlights}
        \end{onecolentry}
"""


def get_skills(skills):
    string = r""
    string += r"""
    \section{Skills}
    \begin{onecolentry}
        \begin{highlightsforbulletentries}
    """
    # print(type(skills))
    for key, value in skills.items():
        formatted_skills = ', '.join(value)
        string += f"\\item \\textbf{{{key}}}: {formatted_skills}"+"\n"
    string += r"""
            \end{highlightsforbulletentries}
    \end{onecolentry}
    """
    return string

def get_experience(experience):
    string = r"""
    \section{Experience}
    """
    for item in experience:
        string += r"\begin{twocolentry}{"
        string += item["duration"] + "}"
        string += r"""
        \textbf{"""
        string += item["company"] + "}, "
        string += r"""
        \end{twocolentry}
        """
        string += r"\textit{"
        string += item["title"] + "}"
        string += r"""
        \vspace{0.10 cm}
        \begin{onecolentry}
        
        """
        string += r"\begin{highlights}"
        for responsibility in item["responsibilities"]:
            string += r"\item " + responsibility.replace("%", "\\%")
        string += r"""
        
        
        \end{highlights}
        \end{onecolentry}
        """
    return string
        

def get_projects(experiences):
    string = r"""
   \section{Projects}
    """
    for item in experiences:
        string += r"""\begin{twocolentry}{
            """
        if item["github_link"] != "":
            string += r"""\href{"""
            string += item["github_link"]
            string += r"""}{Github Link}
            """
        string += r"""}
            \textbf{
                """
        string += item["name"]
                
        string += r"""}
        \end{twocolentry}
        
        \vspace{0.10 cm}
        \begin{onecolentry}
            \begin{highlights}
        """
        for detail in item["details"]:
            string += r"\item " + detail.replace("%", "\\%")
        
        string += r"""
        
        
        \end{highlights}
        \end{onecolentry}
        """
    return string

def get_certificates(certificates):
    string = r"""
   \section{Certificates}
    """
    for item in certificates:
        string += r"""\begin{twocolentry}{
            """
        string += item["date"]
        string += r"""}
            \textbf{
                """
        string += item["issued_by"]
        string += r"""}\end{twocolentry}
        """
        string += item["name"]
        string += r"""
        \vspace{0.2 cm}

        \begin{onecolentry}
        """
        string += item["description"]
        string += r"""\end{onecolentry}"""
    return string

def get_end():
    return r"""
\end{document}
 """