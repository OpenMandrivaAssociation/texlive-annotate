%global tl_name annotate
%global tl_revision 76790

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A bibliography style with annotations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/misc/annotate.bst
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/annotate.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The style is a derivative of the standard alpha style, which processes
an entry's annotate field as part of the printed output.

