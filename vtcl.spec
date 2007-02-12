Summary:	A cross-platform application development environment
Summary(es.UTF-8):   Visual Tcl - Ambiente de desarrollo de aplicaciones multi plataforma
Summary(pl.UTF-8):   Niezależne od platformy środowisko programistyczne
Summary(pt_BR.UTF-8):   Visual Tcl - ambiente de desenvolvimento de aplicações multi-plataforma
Name:		vtcl
Version:	1.6.0b2
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/vtcl/%{name}-%{version}.tar.gz
# Source0-md5:	cf66b0ed8e9144a1ef9e8a2c070489db
Source1:	vtsetup
Source2:	%{name}
Source3:	%{name}.desktop
Source4:	%{name}.png
Patch0:		%{name}-config.patch
URL:		http://www.neuron.com/stewart/vtcl/
Requires:	tk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Visual Tcl is a freely-available, high-quality application development
environment for Unix, Windows and Macintosh platforms. Since it was
written entirely in Tcl (no external libraries required) and generates
pure Tcl, porting should be either unnecessary or trivial. Visual Tcl
includes extensible widget and geometry manager support, support for
the creation of compound widgets and widget libraries, a GUI interface
for most aspects of Tcl/Tk development, and support for the
importation of pre-existing Tcl/Tk code. Visual Tcl can export Tclets,
which will run in Netscape or MSIE.

%description -l es.UTF-8
Visual Tcl - Ambiente de desarrollo de aplicaciones multi plataforma

%description -l pl.UTF-8
Visual Tcl jest darmowym, wysokiej jakości środowiskiem
programistycznym dla Uniksa, Windows i Macintosha. Ponieważ jest ono
napisane w całości w Tcl-u (nie są potrzebne żadne zewnętrzne
biblioteki) i generuje czysty kod Tcl, zmiany w kodzie przy
przenoszeniu na inną platformę powinny być niepotrzebne, lub
trywialne. Visual Tcl posiada interfejs typu GUI dla większości
zagadnień programowania w Tcl/Tk, daje możliwość tworzenia złożonych
widgetów oraz bibliotek widgetów, umożliwia także importowanie
istniejącego kodu Tcl/Tk. Visual Tcl może eksportować tzw. Tclet-y,
które można uruchomić w przeglądarce internetowej (np. Netscape, lub
MSIE).

%description -l pt_BR.UTF-8
O Visual Tcl é um ambiente de desenvolvimento de aplicações para as
plataformas UNIX, Windows e Macintosh, de alta qualidade e livremente
distribuível. Escrito inteiramente em Tcl e gerando código Tcl puro,
torna o porte desnecessário ou trivial.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/lib/vtcl} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cp -a vtcl.tcl images lib $RPM_BUILD_ROOT%{_prefix}/lib/vtcl
install vtsetup.tcl $RPM_BUILD_ROOT%{_prefix}/lib/vtcl
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/vtsetup
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/vtcl
%attr(755,root,root) %{_bindir}/vtsetup
%dir %{_prefix}/lib/vtcl
%{_prefix}/lib/vtcl/lib
%{_prefix}/lib/vtcl/images
%{_prefix}/lib/vtcl/vtcl.tcl
%attr(755,root,root) %{_prefix}/lib/vtcl/vtsetup.tcl
%{_desktopdir}/vtcl.desktop
%{_pixmapsdir}/vtcl.png
