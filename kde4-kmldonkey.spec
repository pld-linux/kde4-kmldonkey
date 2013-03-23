%define		orgname		kmldonkey
%define		qtver		4.7.1
%define		kdever		4.9.0

Summary:	KDE frontend for MLDonkey
Summary(pl.UTF-8):	Interfejs do MLDonkey dla KDE.
Name:		kde4-kmldonkey
Version:	2.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications
# Source0:	%{orgname}-20130301.tgz
# snn checkout svn://anonsvn.kde.org/home/kde/trunk/extragear/network/kmldonkey
Source0:	http://beauty.ant.gliwice.pl/PLD/kmldonkey-20130301.tgz
# Source0-md5:	1555f5863939be55e712f7e6b265b99f
URL:		http://www.kde.org/applications/internet/kmldonkey/development
# leave only required ones, note kde4-kdelibs-devel requires already a bunch full of them
#BuildRequires:	Qt3Support-devel >= %{qtver}
#BuildRequires:	QtCore-devel >= %{qtver}
#BuildRequires:	QtDBus-devel >= %{qtver}
#BuildRequires:	QtDesigner-devel >= %{qtver}
#BuildRequires:	QtGui-devel >= %{qtver}
#BuildRequires:	QtScript-devel >= %{qtver}
#BuildRequires:	QtSvg-devel >= %{qtver}
#BuildRequires:	QtTest-devel >= %{qtver}
#BuildRequires:	QtUiTools-devel >= %{qtver}
#BuildRequires:	QtXml-devel >= %{qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdebase-workspace-devel >= %{kdever}
BuildRequires:	kde4-kdelibs-devel >= %{kdever}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMLDonkey is a KDE frontend for MLDonkey, a powerful P2P file sharing
tool.

%description -l pl.UTF-8
KMLDonkey jest intefejsem dla MLDonkey, poteznego narzedzia wymiany
plikow P2P, przeznaczonym dla KDE.

%prep
%setup -q -n %{orgname}

%build
install -d build
cd build
%cmake \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install/fast \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmldonkey
%attr(755,root,root) %{_libdir}/liblibkmldonkey.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblibkmldonkey.so.5
%attr(755,root,root) %{_libdir}/kde4/plasma_applet_kmldonkey.so
%attr(755,root,root) %{_libdir}/kde4/plasma_engine_kmldonkey.so
%{_desktopdir}/kde4/*.desktop
%{_iconsdir}/*/*/*/*.png
%dir %{_datadir}/apps/kmldonkey
%{_datadir}/apps/kmldonkey/icons
%{_datadir}/apps/kmldonkey/kmldonkeyui.rc
%{_datadir}/apps/kmldonkey/kmldonkey.notifyrc
%{_datadir}/kde4/services/*.desktop

# -devel
# %attr(755,root,root) %ghost %{_libdir}/liblibkmldonkey.so
# /*.h
