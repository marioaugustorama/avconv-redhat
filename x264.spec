%global api 148

Name:           x264-snapshot-20150825
Version:        2245
Release:        1%{?dist}
Summary:        Library for encoding and decoding H264/AVC video streams

Group:          System Environment/Libraries
License:        GPL
URL:            http://developers.videolan.org/x264.html
Source0:        last_x264.tar.bz2

BuildRequires:  gettext
BuildRequires:  yasm
BuildRequires:  nasm

%description
x264 is a free library for encoding H264/AVC video streams, written from
scratch.


%package libs
Summary: Library for encoding H264/AVC video streams
Group: Development/Libraries


%description libs
x264 is a free library for encoding H264/AVC video streams, written from
scratch.

%package devel
Summary: Development files for the x264 library
Group: Development/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: pkgconfig


%description devel
x264 is a free library for encoding H264/AVC video streams, written from
scratch.


%prep
%setup -q


%build
./configure \
	--prefix="%{_prefix}" \
	--libdir="%{_libdir}" \
	--enable-static \
	--enable-shared 

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING
%{_bindir}/x264
%{_libdir}/libx264.so.*

%files devel
%defattr(-, root, root, 0755)
%doc doc/*.txt
%{_includedir}/x264.h
%{_includedir}/x264_config.h
%{_libdir}/pkgconfig/x264.pc
%{_libdir}/libx264.a
%{_libdir}/libx264.so

%files libs
%defattr(644, root, root, 0755)
%{_libdir}/libx264.so.%{api}


%changelog
