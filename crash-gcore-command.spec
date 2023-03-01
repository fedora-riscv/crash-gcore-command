%global reponame crash-gcore

Summary: Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.6.4
Release: 0%{?dist}
License: GPLv2
Source0: https://github.com/fujitsu/crash-gcore/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-gcore
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le x86_64
BuildRequires: crash-devel >= 5.1.5
BuildRequires: gcc
Requires: crash >= 5.1.5

%description
Command for creating a core dump file of a user-space task that was
running in a kernel dump file.

%prep
%autosetup -n %{reponame}-%{version} -p1

%build
%make_build -C src -f gcore.mk

%install
install -m 0755 -d %{buildroot}%{_libdir}/crash/extensions
install -m 0755 -t %{buildroot}%{_libdir}/crash/extensions %{_builddir}/%{reponame}-%{version}/src/gcore.so

%files
%dir %{_libdir}/crash
%dir %{_libdir}/crash/extensions
%{_libdir}/crash/extensions/gcore.so
%license COPYING

%changelog
* Wed Mar 1 2023 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.4-0
- Update to latest upstream release

* Tue Jul 26 2022 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.3-2
- gcore.mk: fix mismatch of _FILE_OFFSET_BITS when building gcore.so
- coredump: fix unexpected truncation of generated core files
- elf: fix warning message caused by type mismatch of offset types
- coredump: fix segmentation fault caused by type mismatch
- x86: Fix failure of collecting vsyscall mapping due to change of enum type of vsyscall_mode
- gcore: fix memory allocation failure during processing NT_AUXV note
- gcore, defs: remove definitions and initializations for saved_auxv entries of offset and size tables
- coredump: use MEMBER_{OFFSET, SIZE} instead of GCORE_{OFFSET, SIZE}

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.3-0
- Update to latest upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.2-1
- Initial crash-gcore-command package
