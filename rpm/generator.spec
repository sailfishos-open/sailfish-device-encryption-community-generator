Name:       sailfish-device-encryption-community-generator

Summary:    SystemD Generator for Sailfish Device Encryption
Version:    0.1
Release:    1
Group:      Qt/Qt
License:    GPLv2
URL:        https://github.com/sailfishos-open/sailfish-device-encryption-community-generator
Source0:    %{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  libsfosdevenc-devel
BuildRequires:  cmake

%description
%summary

%prep
%setup -q -n %{name}-%{version}

%build

%cmake . 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_systemdgeneratordir}
install -t %{buildroot}%{_systemdgeneratordir} --mode=755 sailfish-device-encryption-community-generator

%files
%defattr(-,root,root,-)
%{_systemdgeneratordir}
