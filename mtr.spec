Summary: A network diagnostic tool
Name: mtr
Version: 0.75
Release: 5%{?dist}
Epoch:	2
Group: Applications/Internet
License: GPLv2+
URL: http://www.BitWizard.nl/mtr
Source:	ftp://ftp.bitwizard.nl/mtr/%{name}-%{version}.tar.gz
Source1: xmtr.consolehelper
Source2: xmtr.pam
Source3: net-x%{name}.desktop
Patch0: mtr-0.75-fd-flags.path
BuildRequires: ncurses-devel gtk2-devel desktop-file-utils

Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Mtr is a network diagnostic tool that combines ping and traceroute
into one program. Mtr provides two interfaces: an ncurses interface,
useful for using Mtr from a telnet session; and a GTK+ interface for X
(provided in the mtr-gtk package).

%package gtk
Summary: The GTK+ interface for mtr
Group: Applications/Internet
Requires: mtr = %{epoch}:%{version}-%{release}
Requires: usermode >= 1.37

%description gtk
The mtr-gtk package provides the GTK+ interface for the mtr network
diagnostic tool.

%prep
%setup -q
%patch0 -p1 -b .fd-flags

%build
%configure --enable-gtk2
make %{?_smp_mflags} && mv mtr xmtr && make distclean
%configure --without-gtk
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_sbindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
install -m 0755 mtr $RPM_BUILD_ROOT/%{_sbindir}/mtr
make DESTDIR=$RPM_BUILD_ROOT install

install -m 0755 xmtr $RPM_BUILD_ROOT/%{_bindir}/xmtr.bin
install -m 644 img/mtr_icon.xpm $RPM_BUILD_ROOT/usr/share/pixmaps
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/security/console.apps/xmtr
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT/etc/pam.d/xmtr
mkdir -p  $RPM_BUILD_ROOT/%{_bindir}
ln -fs consolehelper $RPM_BUILD_ROOT/%{_bindir}/xmtr

mkdir -p $RPM_BUILD_ROOT/%{_datadir}/applications

desktop-file-install --vendor="fedora"				\
	--dir=${RPM_BUILD_ROOT}/%{_datadir}/applications		\
	%{SOURCE3}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING FORMATS NEWS README SECURITY
%attr(0755,root,root) %{_sbindir}/mtr
%{_mandir}/man8/*

%files gtk
%defattr(-,root,root,-)
%{_datadir}/applications/fedora-net-x%{name}.desktop
%attr(0755,root,root) %{_bindir}/xmtr.bin
%{_bindir}/xmtr
%config(noreplace) %{_sysconfdir}/pam.d/*
%config(noreplace) %{_sysconfdir}/security/console.apps/*
%{_datadir}/pixmaps/mtr_icon.xpm

%changelog
* Fri Sep 25 2009 Adam Tkac <atkac redhat com> 2:0.75-5
- remove unneeded build requires (#525547)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.75-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.75-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Oct 29 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2:0.75-2
- Fixed setting socket flags in ipv4 only environment (#467964)

* Tue Sep 23 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2:0.75-1
- Updated to 0.75
- Removed confusing underflow patch
- Removed format patch bacause of -w option

* Thu Sep 09 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2:0.74-1
- Updated to 0.74

* Tue Sep 02 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2:0.73-2
- Minor fix in the patch underflow

* Wed May 21 2008 Zdenek Prikryl <zprikryl@redhat.com> - 2:0.73-1
- Updated to 0.73
- Fixed mtr-0.69-CVE-2002-0497.patch
- Added build requirement for GTK+

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2:0.72-4
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Marcela Maslanova <mmaslano@redhat.com> - 2:0.72-3
- rebuild for mas rebuild
- check license

* Thu Mar 15 2007 Karsten Hopp <karsten@redhat.com> 2:0.72-2
- rebuild with current gtk2 to add png support (#232013)

* Thu Feb 22 2007 Marcela Maslanova <mmaslano@redhat.com> - 2:0.72-1
- review
- rhbz#226164

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2:0.71-3.1
- rebuild

* Mon Jul 3 2006 Marcela Maslanova <mmaslano@redhat.com> - 2:0.71-3
- bugzilla #195458 – reverse-map bug in mtr and patch - resolving ipv6 hostname correctly

* Tue May 30 2006 Marcela Maslanova <mmaslano@redhat.com> - 2:0.71-2
- underflow solved

* Fri Mar 24 2006 Miroslav Lichvar <mlichvar@redhat.com> - 2:0.71-1
- update to mtr-0.71

* Thu Mar 23 2006 Miroslav Lichvar <mlichvar@redhat.com> - 2:0.70-1
- update to mtr-0.70
- replace s390x patch, drop automake dependency

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 2:0.69-7.2.1
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 2:0.69-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Fri Oct 21 2005 Phil Knirsch <pknirsch@redhat.com> 2:0.69-7
- Fixed xmtr to be installed in /usr/bin instead of /usr/X11R6/bin (#170945)

* Mon Oct 10 2005 Phil Knirsch <pknirsch@redhat.com> 2:0.69-6
- Added missing gtk+-devel BuildPreReq (#168215)

* Fri Oct  7 2005 Tomas Mraz <tmraz@redhat.com> 2:0.69-5
- use include instead of pam_stack in pam config

* Mon Sep 05 2005 Phil Knirsch <pknirsch@redhat.com> 2:0.69-4
- Made the output, especially for reports much more readable (#147865)
- Fixed --address option (#162029)

* Wed Mar 02 2005 Phil Knirsch <pknirsch@redhat.com> 2:0.69-3
- bump release and rebuild with gcc 4

* Thu Feb 10 2005 Karsten Hopp <karsten@redhat.de> 2:0.69-2 
- build with --enable-gtk2 (John Thacker)

* Wed Feb 09 2005 Phil Knirsch <pknirsch@redhat.com> 2:0.69-1
- Updated to mtr-0.69
- Dropped quite a few patches
- Forewardported the CVE patch

* Mon Oct 18 2004 Phil Knirsch <pknirsch@redhat.com> 2:0.54-10
- rebuilt

* Wed Oct 06 2004 Phil Knirsch <pknirsch@redhat.com> 2:0.54-9
- Add CVE patch for security reasons (#129386)
- Add patch to fix broken --address option (#132628)
- Add patch to fix broken reverse DNS lookups for ipv6 (#134532)

* Tue Aug 24 2004 Warren Togami <wtogami@redhat.com> 2:0.54-8
- #121705 and other spec cleanups
- remove redundant documentation

* Thu Jul 01 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-7
- Fixed broken behaviour with resolver SERVFAIL results (#125392)
- Added ncurses-devel libtermcap-devel as BuildPreReq (#124553)
- Added gtk+ Requires for mtr-gtk package (#121705)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 21 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-5
- Removed absolute path for Icon in desktop file (#120170)

* Mon Feb 16 2004 Phil Knirsch <pknirsch@redhat.com>
- Added IPv6 patch from ftp://ftp.kame.net/pub/kame/misc/mtr-054-*
- Enabled IPv6 in mtr.
- Included fix from Robert Scheck to make GTK optional in configure.

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Feb 04 2004 Phil Knirsch <pknirsch@redhat.com> 0.54-2
- Fix to build on current tree.

* Sat Oct 18 2003 Florian La Roche <Florian.LaRoche@redhat.de>
- update to 0.54

* Wed Jun 04 2003 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Jan 22 2003 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Nov 29 2002 Phil Knirsch <pknirsch@redhat.com> 0.52-1
- Update to latest upstream version (0.52).

* Tue Nov 12 2002 Nalin Dahyabhai <nalin@redhat.com> 0.49-9
- Remove absolute paths from the PAM configuration, ensuring that the modules
  for the right arch get used on multilib systems.
- Remove Icon:.

* Tue Sep 24 2002 Bernhard Rosenkraenzer <bero@redhat.com> 0.49-7a
- Fix build on s390x

* Mon Aug 19 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-7
- Fixed consolehelper support.

* Wed Aug 07 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-6
- Desktop file fixes (#69550).

* Fri Jun 21 2002 Tim Powers <timp@redhat.com> 0.49-5
- automated rebuild

* Tue Jun 18 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-4
- Added consolehelper support to xmtr.

* Sun May 26 2002 Tim Powers <timp@redhat.com>
- automated rebuild

* Wed May 22 2002 Phil Knirsch <pknirsch@redhat.com> 0.49-2
- Fixed autoFOO problems.

* Fri Mar 08 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- 0.49 update

* Thu Mar 07 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- 0.48 update

* Mon Jun 25 2001 Preston Brown <pbrown@redhat.com>
- 0.44 bugfix release
- fix display of icon in .desktop entry

* Sun Jun 24 2001 Elliot Lee <sopwith@redhat.com>
- Bump release + rebuild.

* Mon Feb 12 2001 Preston Brown <pbrown@redhat.com>
- don't advertise gtk support in non-gtk binary (#27172)

* Fri Oct 20 2000 Bill Nottingham <notting@redhat.com>
- fix autoconf check for resolver functions

* Fri Jul 21 2000 Bill Nottingham <notting@redhat.com>
- fix group

* Wed Jul 12 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Thu Jul  6 2000 Bill Nottingham <notting@redhat.com>
- fix setuid bit
- remove symlink
- force build of non-gtk version

* Mon Jun 19 2000 Preston Brown <pbrown@redhat.com>
- disable SUID bits
- desktop entry

* Mon Jun 19 2000 Than Ngo <than@redhat.de>
- FHS fixes

* Fri May 26 2000 Preston Brown <pbrown@redhat.com>
- adopted for Winston

* Thu Aug 19 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.41-1]
- Added afr's patch to allow disabeling of gtk without Robn's hack. 
- Made report mode report the newly added extra resolution. 

* Wed Aug 18 1999 Ryan Weaver <ryanw@infohwy.com>
- renamed mtr-gtk to xmtr
- added symlink from /usr/bin/mtr to /usr/sbin/mtr

  [mtr-0.40-1]
- Fixed some problems with HPUX and SunOS.
- Included Olav Kvittem's patch to do packetsize option.
- Made the timekeeping in micro seconds.

* Wed Jun 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.39-1]
- Updated to version 0.39.

* Wed Jun  9 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.38-1]
- Updated to version 0.38.

* Thu Apr 15 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.37-2]
- Changed RPM headers to conform to Red Hat Contrib|Net specs.

* Mon Apr 12 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.37-1]
- v0.37
- Added Bill Bogstad's "show the local host & time" patch. 
- Added R. Sparks' show-last-ping patch, submitted by Philip Kizer.

- v0.36
- Added Craigs change-the-interval-on-the-fly patch.
- Added Moritz Barsnick's "do something sensible if host not found" 
  patch.
- Some cleanup of both Craigs and Moritz' patches.

* Wed Apr  7 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.35-1]
- v0.35
- Added Craig Milo Rogers pause/resume for GTK patch.
- Added Craig Milo Rogers cleanup of "reset". (restart at the beginning)
- Net_open used to send a first packet. After that the display-driver
  got a chance to distort the timing by taking its time to initialize.

* Mon Apr  5 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.34-1]
- v0.34
- Added Matt's nifty "use the icmp unreachables to do the timing" patch.
- Added Steve Kann's pause/resume patch.

* Wed Mar 10 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.33-1]
- v0.33
- Fixed the Linux glibc resolver problems.
- Fixed the off-by-one problem with -c option.

* Mon Mar  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.32-1]
- v0.32
- Fixed the FreeBSD bug detection stuff.

* Fri Mar  5 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.31-1]
- v0.31
- Fixed a few documentation issues. -- Matt
- Changed the autoconf stuff to find the resolver library on
  Solaris. -- REW
- Cleaned up the autoconf.in file a bit. -- Matt.

* Thu Mar  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [mtr-0.30-1]
- Build gtk version against gtk+-1.2.0
- v0.30
- Fixed a typo in the changelog (NEWS) entry for 0.27. :-)
- added use of "MTR_OPTIONS" environment variable for defaults.
