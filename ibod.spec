Summary: Ibod - ISDN MPPP bandwidth on demand daemon
Name: ibod
Version: 1.5.0
Release: 15
Source0: http://www.compound.se/download/%{name}-%{version}-src.tar.bz2
Source1: ibod.service
Patch0: ibod.cf.patch
URL: http://www.compound.se/ibod.html
License: GPL
Group: Networking/Other

%description 
ibod is a ISDN MPPP bandwidth on demand daemon designed to operate
in conjunction with isdn4linux.
It is normally started at boot time, but can be started and stopped
at any time. The program monitors inbound and outbound traffic on
the ISDN interface. When the required bandwidth exceeds the capacity
for one IDSN B-channel (64kbps) a second (slave) channel is connected
according to the MPPP protocol. When the traffic decreases below
one channel capacity, the slave channel is disconnected.

%prep
%setup -q
#%patch0 -p0

%build
%make

%install

mkdir -p %{buildroot}%{_sysconfdir}/ppp
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man4
mkdir -p %{buildroot}%{_sbindir}
install -m755 ibod %{buildroot}%{_sbindir}
install -m644 ibod.1 %{buildroot}%{_mandir}/man1/
install -m644 ibod.cf.4 %{buildroot}%{_mandir}/man4/
install -m644 ibod.cf %{buildroot}%{_sysconfdir}/ppp/
install -m644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service

sed "s:sysconfig:%{_sysconfdir}/sysconfig:" -i %{buildroot}%{_unitdir}/%{name}.service

%clean

%post
%systemd_post ibod

%preun
%systemd_preun ibod

%files
%{_sbindir}/*
%{_mandir}/man1/ibod.1*
%{_mandir}/man4/ibod.cf.4*
%attr(0644,root,root) %{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/ppp/ibod.cf
