Summary: ISDN MPPP bandwidth on demand daemon
Name: ibod
Version: 1.5.0
Release: 13
Source0: http://www.compound.se/download/%{name}-%{version}-src.tar.bz2
Source1: ibod.init
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
mkdir -p %{buildroot}/%{_sysconfdir}/ppp
mkdir -p %{buildroot}/%{_initrddir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_mandir}/man4
mkdir -p %{buildroot}/%{_sbindir}
install -m755 ibod %{buildroot}/%{_sbindir}
install -m644 ibod.1 %{buildroot}/%{_mandir}/man1/
install -m644 ibod.cf.4 %{buildroot}/%{_mandir}/man4/
install -m644 ibod.cf %{buildroot}/%{_sysconfdir}/ppp/
install -m755 %{SOURCE1} %{buildroot}/%{_initrddir}/ibod
ln -s /etc/rc.d/init.d/ibod %{buildroot}/usr/sbin/rcibod

%clean

%post
%_post_service ibod

%preun
%_preun_service ibod

%files
%{_sbindir}/*
%{_mandir}/man1/ibod.1*
%{_mandir}/man4/ibod.cf.4*
%config(noreplace) %{_initrddir}/ibod
%config(noreplace) %{_sysconfdir}/ppp/ibod.cf



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-10mdv2011.0
+ Revision: 665492
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-9mdv2011.0
+ Revision: 605951
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.5.0-8mdv2010.1
+ Revision: 522915
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.5.0-7mdv2010.0
+ Revision: 425196
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.5.0-6mdv2009.1
+ Revision: 351243
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-5mdv2009.0
+ Revision: 221436
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.5.0-4mdv2008.1
+ Revision: 150278
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Sep 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-3mdv2008.0
+ Revision: 89692
- rebuild

* Fri Jul 06 2007 Adam Williamson <awilliamson@mandriva.org> 1.5.0-2mdv2008.0
+ Revision: 48878
- use standard macros for service

* Thu Jul 05 2007 Funda Wang <fwang@mandriva.org> 1.5.0-1mdv2008.0
+ Revision: 48377
- New version


* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 10:04:17 (55927)
- mkrelisation

* Mon Aug 14 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/14/06 10:02:05 (55926)
Import ibod

* Wed Sep 01 2004 Arnaud de Lorbeau <adelorbeau@mandrakesoft.com> 1.4-4mdk
- rebuild for rpm 4.2

