Name:           libav 
Version:        11.4
Release:        1%{?dist}
Summary:        Open source audio and video processing tools

Group:          Applications/Multimedia 
License:        LGPL
URL:            https://libav.org/
Source0:        https://libav.org/releases/libav-11.4.tar.gz
BuildRequires: gcc => 4, /usr/bin/find
BuildRequires: yasm
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: lame-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: libv4l
BuildRequires: openssl-devel
BuildRequires: x264-snapshot-20150825-devel


%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries

%description


%description devel
FFmpeg is a complete and free Internet live audio and video broadcasting
solution for Linux/Unix. It also includes a digital VCR. It can encode in real
time in many formats including MPEG1 audio and video, MPEG4, h263, ac3, asf,
avi, real, mjpeg, and flash.
This package contains development files for ffmpeg

%prep
%setup -q


%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} \
            --shlibdir=%{_libdir} --mandir=%{_mandir} \
	--enable-nonfree --enable-gpl --enable-version3 --enable-bzlib --enable-zlib --enable-libmp3lame --enable-libpulse --enable-vdpau --enable-pthreads --enable-openssl 

make %{?_smp_mflags}



%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Remove from the included docs
rm -f doc/Makefile
rm -f %{buildroot}/usr/share/doc/ffmpeg/*.html
rm -rf %{buildroot}%{_mandir}/man3/
rm -f %{buildroot}%{_libdir}/*.a

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_datadir}/avconv
%{_mandir}/man1/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc

%changelog
