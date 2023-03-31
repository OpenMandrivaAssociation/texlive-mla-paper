Name:		texlive-mla-paper
Version:	54080
Release:	2
Summary:	Proper MLA formatting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mla-paper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mla-paper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mla-paper.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package formats articles using the MLA style. The aim is
that students and other academics in the humanities should be
able to typeset their materials, properly, with minimal effort
on their part.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mla-paper/mla.sty
%doc %{_texmfdistdir}/doc/latex/mla-paper/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
