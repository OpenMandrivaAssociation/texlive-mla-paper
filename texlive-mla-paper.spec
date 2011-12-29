# revision 20885
# category Package
# catalog-ctan /macros/latex/contrib/mla-paper
# catalog-date 2010-12-30 15:21:17 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-mla-paper
Version:	20101230
Release:	1
Summary:	Proper MLA formatting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mla-paper
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mla-paper.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mla-paper.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
