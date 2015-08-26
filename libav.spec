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

%description


%prep
%setup -q


%build
./configure \
	--enable-gpl \
	--enable-nonfree \
	--enable-version3

make 


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog
