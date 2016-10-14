%if 0%{?fedora}
%global with_python3 1
%endif

%global pypi_name XStatic-jQuery

Name:           python-%{pypi_name}
Version:        1.10.2.1
Release:        5%{?dist}
Summary:        jQuery (XStatic packaging standard)

License:        MIT
URL:            http://jquery.com/
Source0:        https://files.pythonhosted.org/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: web-assets-devel

%description
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

%package -n python2-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

Requires:       python2-XStatic
Requires:       js-jquery1

%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 2 build of %{pypi_name}.

%if 0%{?with_python3}
%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       js-jquery1

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JavaScript library packaged for setuptools (easy_install) / pip.

This package is intended to be used by any project that needs these files.

It intentionally does not provide any extra code except some metadata
nor has any extra requirements.

This package provides Python 3 build of %{pypi_name}.
%endif


%prep
%autosetup -n %{pypi_name}-%{version}
# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/jquery/1'|" xstatic/pkg/jquery/__init__.py

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

rm -rf %{buildroot}%{python2_sitelib}/xstatic/pkg/jquery/data/


%if 0%{?with_python3}
%py3_install
# Remove static files, already created by the python2 subpkg
rm -rf %{buildroot}%{python3_sitelib}/xstatic/pkg/jquery/data
%endif

%files -n python2-%{pypi_name}
%doc README.txt
%{python2_sitelib}/xstatic/pkg/jquery
%{python2_sitelib}/XStatic_jQuery-%{version}-py%{python2_version}.egg-info
%{python2_sitelib}/XStatic_jQuery-%{version}-py%{python2_version}-nspkg.pth

%if 0%{?with_python3}
%files -n python3-%{pypi_name}
%doc README.txt
%{python3_sitelib}/xstatic/pkg/jquery
%{python3_sitelib}/XStatic_jQuery-%{version}-py%{python3_version}.egg-info
%{python3_sitelib}/XStatic_jQuery-%{version}-py%{python3_version}-nspkg.pth
%endif


%changelog
* Thu Oct 13 2016 Jan Beran <jberan@redhat.com> - 1.10.2.1-5
- Provides a Python 3 subpackage
- depend on js-jquery1 rather than bundling its own

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2.1-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Mar 12 2014 Matthias Runge <mrunge@redhat.com> - 1.10.2.1-1
- Initial package.
