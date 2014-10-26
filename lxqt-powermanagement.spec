#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-powermanagement
Name:		lxqt-powermanagement
Version:	0.8.0
Release:	0.2
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	3dfb506a077a36b822389f4679c824c9
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Svg-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.8.0
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	libxcb-devel
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-powermanagement.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
    -DUSE_QT5=ON \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-powermanagement
%attr(755,root,root) %{_bindir}/lxqt-powermanagement
%{_desktopdir}/lxqt-config-powermanagement.desktop
%{_iconsdir}/hicolor/scalable/devices/laptop-lid.svg
