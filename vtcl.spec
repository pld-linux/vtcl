Summary:	A cross-platform application development environment
Summary(es):	Visual Tcl - Ambiente de desarrollo de aplicaciones multi plataforma
Summary(pl):	Niezale¿ne od platformy ¶rodowisko programistyczne
Summary(pt_BR):	Visual Tcl - ambiente de desenvolvimento de aplicações multi-plataforma
Name:		vtcl
Version:	1.6.0b2
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
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

%description -l es
Visual Tcl - Ambiente de desarrollo de aplicaciones multi plataforma

%description -l pl
Visual Tcl jest darmowym, wysokiej jako¶ci ¶rodowiskiem
programistycznym dla Unix-a, Windows i Macintosh-a. Poniewa¿ jest ono
napisane w ca³o¶ci w Tcl (nie s± potrzebne ¿adne zewnêtrzne
biblioteki) i generuje czysty kod Tcl, zmiany w kodzie przy
przenoszeniu na inn± platformê powinny byæ niepotrzebne, lub
trywialne. Visual Tcl posiada interfejs typu GUI dla wiêkszo¶ci
zagadnieñ programowania w Tcl/Tk, daje mo¿liwo¶æ tworzenia z³o¿onych
widgetów oraz bibliotek widgetów, umo¿liwia tak¿e importowanie
istniej±cego kodu Tcl/Tk. Visual Tcl mo¿e eksportowaæ tzw. Tclet-y,
które mo¿na uruchomiæ w przegl±darce internetowej (np. Netscape, lub
MSIE).

%description -l pt_BR
O Visual Tcl é um ambiente de desenvolvimento de aplicações para as
plataformas UNIX, Windows e Macintosh, de alta qualidade e livremente
distribuível. Escrito inteiramente em Tcl e gerando código Tcl puro,
torna o porte desnecessário ou trivial.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/vtcl} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

cp -ar vtcl.tcl images lib $RPM_BUILD_ROOT%{_libdir}/vtcl/
install vtsetup.tcl $RPM_BUILD_ROOT%{_libdir}/vtcl/
install %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/vtsetup
install %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/
install %{SOURCE3} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE4} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README doc/*
%attr(755,root,root) %{_bindir}/vtcl
%attr(755,root,root) %{_bindir}/vtsetup
%dir %{_libdir}/vtcl
%{_libdir}/vtcl/lib
%{_libdir}/vtcl/images
%{_libdir}/vtcl/vtcl.tcl
%attr(755,root,root) %{_libdir}/vtcl/vtsetup.tcl
%{_desktopdir}/vtcl.desktop
%{_pixmapsdir}/vtcl.png
