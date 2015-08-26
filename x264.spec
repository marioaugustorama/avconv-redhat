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


%prep
%setup -q


%build
./configure \
	--enable-static \
	--enable-shared 

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
