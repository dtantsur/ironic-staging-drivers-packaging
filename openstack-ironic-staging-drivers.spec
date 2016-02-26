%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%global orig_name ironic-staging-drivers
%global module ironic_staging_drivers

Name:       openstack-%{orig_name}
Version:    XXX
Release:    XXX
Summary:    Staging drivers for OpenStack Ironic
License:    ASL 2.0
URL:        http://launchpad.net/%{orig_name}/

Source0:    http://tarballs.openstack.org/%{orig_name}/%{orig_name}-master.tar.gz

BuildArch:  noarch

%package -n openstack-%{orig_name}
Summary:    Staging drivers for OpenStack Ironic

BuildRequires:  python2-devel
BuildRequires:  python-pbr
BuildRequires:  python-setuptools
BuildRequires:  git

Requires:   python-oslo-i18n
Requires:   python-oslo-utils

%description -n openstack-%{orig_name}
The Ironic Staging Drivers is used to hold out-of-tree Ironic drivers
which doesn't have means to provide a 3rd Party CI at this point in
time which is required by Ironic.

The intention of this project is to provide a common place for useful
drivers resolving the "hundreds of different download sites" problem.


%package -n openstack-%{orig_name}-tests
Summary:    Staging drivers for OpenStack Ironic - tests
Requires:   openstack-%{orig_name} = %{version}-%{release}

%description -n openstack-%{orig_name}-tests
The Ironic Staging Drivers is used to hold out-of-tree Ironic drivers
which doesn't have means to provide a 3rd Party CI at this point in
time which is required by Ironic.

The intention of this project is to provide a common place for useful
drivers resolving the "hundreds of different download sites" problem.

This package contains the test files.


%package -n openstack-%{orig_name}-doc
Summary:    Staging drivers for OpenStack Ironic - documentation

BuildRequires: python-sphinx
BuildRequires: python-oslo-sphinx

%description -n openstack-%{orig_name}-doc
The Ironic Staging Drivers is used to hold out-of-tree Ironic drivers
which doesn't have means to provide a 3rd Party CI at this point in
time which is required by Ironic.

The intention of this project is to provide a common place for useful
drivers resolving the "hundreds of different download sites" problem.

This package contains the documentation.


%description
The Ironic Staging Drivers is used to hold out-of-tree Ironic drivers
which doesn't have means to provide a 3rd Party CI at this point in
time which is required by Ironic.

The intention of this project is to provide a common place for useful
drivers resolving the "hundreds of different download sites" problem.


%prep
%autosetup -n %{orig_name}-%{upstream_version} -S git

# Let's handle dependencies ourseleves
rm -f *requirements.txt

%build
%py2_build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py2_install

%check
%{__python2} setup.py test

%files -n openstack-%{orig_name}
%license LICENSE
%{python2_sitelib}/%{module}
%{python2_sitelib}/%{module}-*.egg-info
%exclude %{python2_sitelib}/%{module}/tests

%files -n openstack-%{orig_name}-tests
%license LICENSE
%{python2_sitelib}/%{module}/tests

%files -n openstack-%{orig_name}-doc
%license LICENSE
%doc html README.rst

%changelog
