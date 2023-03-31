Name:		texlive-register
Version:	54485
Release:	2
Summary:	Typeset programmable elements in digital hardware (registers)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/register
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/register.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/register
%doc %{_texmfdistdir}/doc/latex/register
#- source
%doc %{_texmfdistdir}/source/latex/register

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
