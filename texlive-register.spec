# revision 21127
# category Package
# catalog-ctan /macros/latex/contrib/register
# catalog-date 2011-01-19 22:37:08 +0100
# catalog-license lppl
# catalog-version 1.6
Name:		texlive-register
Version:	1.6
Release:	11
Summary:	Typeset programmable elements in digital hardware (registers)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/register
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is designed for typesetting the programmable
elements in digital hardware, i.e., registers. Such registers
typically have many fields and can be quite wide; they are thus
a challenge to typeset in a consistent manner. Register is
similar in some aspects to the bytefield package. Anyone doing
hardware documentation using LaTeX should examine both
packages. Register requires a fairly recent version of the
float package. A Perl module and a Perl script are provided, to
translate the register specifications into programmable data
structures.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/register/register.sty
%doc %{_texmfdistdir}/doc/latex/register/Reg_macro.pm
%doc %{_texmfdistdir}/doc/latex/register/reg_list.pl
%doc %{_texmfdistdir}/doc/latex/register/register.pdf
#- source
%doc %{_texmfdistdir}/source/latex/register/register.dtx
%doc %{_texmfdistdir}/source/latex/register/register.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.6-2
+ Revision: 755656
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.6-1
+ Revision: 719446
- texlive-register
- texlive-register
- texlive-register
- texlive-register

