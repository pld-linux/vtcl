Summary:	A cross-platform application development environment.
Summary:	Niezale¿ne od platformy ¶rodowisko programistyczne.
Name:		vtcl
Version:	1.5.1b3
Release:	1
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://prdownloads.sourceforge.net/vtcl/%{name}-%{version}.tar.gz
Source1:	vtsetup
URL:		http://www.neuron.com/stewart/vtcl/
Patch0:		%{name}-config.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	tcl tk
BuildArch:	noarch

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

%description -l pl
Visual Tcl jest darmowym, wysokiej jako¶ci ¶rodowiskiem
programistycznym dla Unix-a, Windows i Macintosh-a. Poniewa¿ jest ono
napisane w ca³o¶ci w Tcl (nie s± potrzebne ¿adne zewnêtrzne biblioteki)
i generuje czysty kod Tcl, zmiany w kodzie przy przenoszeniu na inn± 
platformê powinny byæ niepotrzebne, lub  trywialne. Visual Tcl posiada
interfejs typu GUI dla wiêkszo¶ci zagadnieñ programowania w Tcl/Tk,
daje mo¿liwo¶æ tworzenia z³o¿onych widgetów oraz bibliotek widgetów, 
umo¿liwia tak¿e importowanie istniej±cego kodu Tcl/Tk.
Visual Tcl mo¿e eksportowaæ tzw. Tclet-y, które mo¿na uruchomiæ w 
przegl±darce internetowej (np. Netscape, lub MSIE).

%prep
%setup -q
%patch0 -p1 
%{__install} %{SOURCE1} .

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/vtcl}
cp -ar vtcl.tcl images lib $RPM_BUILD_ROOT%{_libdir}/vtcl/
%{__install} -m 755 vtsetup.tcl $RPM_BUILD_ROOT%{_libdir}/vtcl/
%{__install} vtcl $RPM_BUILD_ROOT%{_bindir}/
%{__install}  vtsetup $RPM_BUILD_ROOT%{_bindir}/vtsetup

gzip -9nf LICENSE README doc/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.gz
%attr(755,root,root) %{_bindir}/vtcl
%attr(755,root,root) %{_bindir}/vtsetup
%{_libdir}/vtcl/lib
%{_libdir}/vtcl/images
%{_libdir}/vtcl/vtcl.tcl
%attr(755,root,root) %{_libdir}/vtcl/vtsetup.tcl
