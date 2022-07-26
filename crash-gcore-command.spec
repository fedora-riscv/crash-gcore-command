%global reponame crash-gcore

Summary: Gcore extension module for the crash utility
Name: crash-gcore-command
Version: 1.6.3
Release: 1%{?dist}
License: GPLv2
Source0: https://github.com/fujitsu/crash-gcore/archive/v%{version}/%{name}-%{version}.tar.gz
URL: https://github.com/fujitsu/crash-gcore
ExclusiveOS: Linux
ExclusiveArch: aarch64 ppc64le x86_64
BuildRequires: crash-devel >= 5.1.5
BuildRequires: gcc
Requires: crash >= 5.1.5

Patch0: crash-gcore-1.6.3-coredump-use-MEMBER_-OFFSET-SIZE-instead-of-GCORE_-O.patch
Patch1: crash-gcore-1.6.3-gcore-defs-remove-definitions-and-initializations-fo.patch
Patch2: crash-gcore-1.6.3-gcore-fix-memory-allocation-failure-during-processin.patch
Patch3: crash-gcore-1.6.3-x86-Fix-failure-of-collecting-vsyscall-mapping-due-t.patch
Patch4: crash-gcore-1.6.3-coredump-fix-segmentation-fault-caused-by-type-misma.patch
Patch5: crash-gcore-1.6.3-elf-fix-warning-message-caused-by-type-mismatch-of-o.patch
Patch6: crash-gcore-1.6.3-coredump-fix-unexpected-truncation-of-generated-core.patch
Patch7: crash-gcore-1.6.3-gcore.mk-fix-mismatch-of-_FILE_OFFSET_BITS-when-buil.patch

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
* Tue Jul 26 2022 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.3-1
- gcore.mk: fix mismatch of _FILE_OFFSET_BITS when building gcore.so
- coredump: fix unexpected truncation of generated core files
- elf: fix warning message caused by type mismatch of offset types
- coredump: fix segmentation fault caused by type mismatch
- x86: Fix failure of collecting vsyscall mapping due to change of enum type of vsyscall_mode
- gcore: fix memory allocation failure during processing NT_AUXV note
- gcore, defs: remove definitions and initializations for saved_auxv entries of offset and size tables
- coredump: use MEMBER_{OFFSET, SIZE} instead of GCORE_{OFFSET, SIZE}

* Fri Dec 10 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.3-0
- Update to latest upstream release

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jan 22 2021 HATAYAMA Daisuke <d.hatayama@fujitsu.com> - 1.6.2-1
- Initial crash-gcore-command package
