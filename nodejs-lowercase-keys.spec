%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# ava module not in fedora yet
%global enable_tests 0
%global module_name lowercase-keys

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        1.0.0
Release:        6%{?dist}
Summary:        Lowercase the keys of an object

License:        MIT
URL:            https://github.com/sindresorhus/lowercase-keys
Source0:        https://github.com/sindresorhus/lowercase-keys/archive/v%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}runtime

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(ava)
%endif

%description
%{summary}.

%prep
%setup -q -n %{module_name}-%{version}
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
node test.js
%endif

%files
%{!?_licensedir:%global license %doc}
%doc readme.md
%license license
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-5
- Rebuilt with updated metapackage

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-4
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 1.0.0-3
- Enable scl macros, fix license macro for el6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 31 2015 Parag Nemade <pnemade AT redhat DOT com> - 1.0.0-1
- Initial packaging