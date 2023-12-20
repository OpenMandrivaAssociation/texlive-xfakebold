Name:		texlive-xfakebold
Version:	68929
Release:	1
Summary:	Fake a regular font for bold characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xfakebold
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfakebold.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xfakebold.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses PDF's text rendering to modify the linewidth
of an outline font to get bold characters. It works only for
vectorfonts where the glyphs are defined by their outline. The
package works both in text and in math mode, for pdfLaTeX as
well as for LuaLaTeX. The package depends on ifluatex, ifxetex,
and xkeyval.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/xfakebold
%doc %{_texmfdistdir}/doc/latex/xfakebold

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
