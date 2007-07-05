Summary: Ibod - ISDN MPPP bandwidth on demand daemon
Name: ibod
Version: 1.5.0
Release: %mkrel 1
Source0: http://www.compound.se/download/%{name}-%{version}-src.tar.bz2
Source1: ibod.init
Patch0: ibod.cf.patch
URL: http://www.compound.se/ibod.html
License: GPL
Group: Networking/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

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
rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/ppp
mkdir -p $RPM_BUILD_ROOT/%{_initrddir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man4
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
install -m755 ibod $RPM_BUILD_ROOT/%{_sbindir}
install -m644 ibod.1 $RPM_BUILD_ROOT/%{_mandir}/man1/
install -m644 ibod.cf.4 $RPM_BUILD_ROOT/%{_mandir}/man4/
install -m644 ibod.cf $RPM_BUILD_ROOT/%{_sysconfdir}/ppp/
install -m755 %{SOURCE1} $RPM_BUILD_ROOT/%{_initrddir}/ibod
ln -s /etc/rc.d/init.d/ibod $RPM_BUILD_ROOT/usr/sbin/rcibod

%clean
rm -rf $RPM_BUILD_ROOT

%post
chkconfig --add ibod

%preun
[ -f /var/lock/subsys/ibod  ] && /etc/rc.d/init.d/ibod stop
/sbin/chkconfig --del ibod

%files
%defattr(-,root,root)
%{_sbindir}/*
%{_mandir}/man1/ibod.1*
%{_mandir}/man4/ibod.cf.4*
%config(noreplace) %{_initrddir}/ibod
%config(noreplace) %{_sysconfdir}/ppp/ibod.cf

