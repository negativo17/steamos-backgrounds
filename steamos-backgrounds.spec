Name:           steamos-backgrounds
Version:        0.7
Release:        1%{?dist}
Summary:        Valve themed wallpapers

License:        BSD
URL:            http://store.steampowered.com/steamos/
Source0:        http://repo.steampowered.com/steamos/pool/main/v/valve-wallpapers/valve-wallpapers_%{version}.tar.gz

BuildArch:      noarch

%description
A collection of Valve themed wallpapers that can be used in the gnome desktop
environment.

%prep
%setup -q -n valve-wallpapers

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/
install -p -m 644 .%{_datadir}/backgrounds/* %{buildroot}%{_datadir}/backgrounds/

install -p -m 644 -D .%{_datadir}/gnome-background-properties/valve-wallpapers.xml \
    %{buildroot}%{_datadir}/gnome-background-properties/valve-wallpapers.xml

%files
%doc debian/copyright debian/changelog
%{_datadir}/backgrounds/*
%{_datadir}/gnome-background-properties/*

%changelog
* Sun Jun  8 2014 Simone Caronni <negativo17@gmail.com> - 0.7-1
- First build.
