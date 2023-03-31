Name:		texlive-annotate
Version:	52824
Release:	2
Summary:	A bibliography style with annotations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/annotate
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The style is a derivative of the standard alpha style, which
processes an entry's annotate field as part of the printed
output.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/annotate

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
