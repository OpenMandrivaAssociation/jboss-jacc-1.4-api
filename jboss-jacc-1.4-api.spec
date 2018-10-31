%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jacc-1.4-api
Version:          1.0.2
Release:          8.3
Summary:          JBoss JACC 1.4 API
Group:		  Development/Java
License:          CDDL or GPLv2 with exceptions
URL:              http://www.jboss.org

# git clone git://github.com/jboss/jboss-jacc-api_spec.git jboss-jacc-1.4-api
# cd jboss-jacc-1.4-api/ && git archive --format=tar --prefix=jboss-jacc-1.4-api/ jboss-jacc-api_1.4_spec-1.0.2.Final | xz > jboss-jacc-1.4-api-1.0.2.Final.tar.xz

Source0:          %{name}-%{namedversion}.tar.xz

BuildRequires:    java-devel
BuildRequires:    jboss-servlet-3.0-api
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-surefire-provider-junit4

Requires:         java
Requires:         jpackage-utils
Requires:         jboss-servlet-3.0-api

BuildArch:        noarch

%description
JBoss Java Authorization Contract for Containers 1.4 API

%package javadoc
Summary:          Javadocs for %{name}

Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README LICENSE

%files javadoc -f .mfiles-javadoc
%doc LICENSE README

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.0.2-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Aug 6 2012 Ricardo Arguello <ricardo@fedoraproject.org> 1.0.2-3
- Added BR: maven-enforcer-plugin

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Apr 04 2012 Marek Goldmann <mgoldman@redhat.com> 1.0.2-1
- Upstream release 1.0.2.Final
- Fixed R and BR

* Tue Apr 3 2012 Ricardo Arguello <ricardo@fedoraproject.org> 1.0.2-0.2.20120310git7976d2
- Removed jboss-specs-parent as a runtime requirement
- Removed duplicated jboss-servlet-3.0-api as a build requirement

* Sat Mar 10 2012 Ricardo Arguello <ricardo@fedoraproject.org> 1.0.2-0.1.20120310git7976d2
- Packaging after license cleanup upstream

* Thu Mar 8 2012 Ricardo Arguello <ricardo@fedoraproject.org> 1.0.1-2
- Cleanup of the spec file

* Mon Nov 21 2011 Marek Goldmann <mgoldman@redhat.com> 1.0.1-1
- Initial packaging
