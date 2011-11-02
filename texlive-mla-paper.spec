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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
The package formats articles using the MLA style. The aim is
that students and other academics in the humanities should be
able to typeset their materials, properly, with minimal effort
on their part.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
