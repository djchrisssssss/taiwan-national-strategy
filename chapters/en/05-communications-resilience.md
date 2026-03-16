# Chapter 5: Communications Resilience — Submarine Cables, LEO Satellites, and Mesh Networks

> **Key Thesis**: Taiwan's external communications are overwhelmingly concentrated on submarine cables, creating a strategic single point of vulnerability. Constructing a multi-layered architecture encompassing LEO satellites, radio backup systems, and community-level mesh networks is essential to maintaining minimum communications capability under crisis scenarios.

---

## 5.1 Submarine Cable Infrastructure

### Background

As an island economy, Taiwan relies almost entirely on submarine cables for its external communications. Approximately 99% of global intercontinental data traffic is transmitted via submarine cables, with satellite communications handling only a marginal share. This means submarine cables are not merely commercial communications infrastructure — they are a critical national security lifeline.

Data from the International Telecommunication Union (ITU) indicates that more than 500 submarine cables are currently in operation worldwide, with a combined length exceeding 1.3 million kilometers. Within this global network, Taiwan occupies a key node position in the western Pacific, serving as a conduit for data flows between Northeast and Southeast Asia.

### Current Assessment

Taiwan currently has approximately fifteen major submarine cables connecting it to the global internet. The principal landing stations are concentrated in the following areas:

| Landing Station Location | Connection Direction | Major Cable Systems | Notes |
|--------------------------|---------------------|--------------------|----|
| Tamsui, New Taipei City | Japan, United States | APG, FASTER | Primary northbound node |
| Bali, New Taipei City | Japan, South Korea | TGN-IA, NCP | Northeast Asia connection |
| Fangliao, Pingtung | Philippines, Singapore, Hong Kong | AAG, SJC, SEA-ME-WE | Primary southbound node |
| Toucheng, Yilan | Japan, Guam | APCN2, PLCN | Eastbound Pacific connection |

This configuration exhibits the following characteristics:

1. **Geographic concentration**: The limited number of landing stations, clustered at a few coastal locations, forms predictable targets for attack.
2. **Route interdependence**: Multiple cables share proximate seabed paths, particularly in the southern Taiwan Strait and the Bashi Channel.
3. **Repair bottlenecks**: The global fleet of cable repair ships is limited (approximately 60 vessels), and repair response times in waters surrounding Taiwan are constrained by vessel scheduling and weather conditions.

### Risk Analysis

Threats to submarine cables can be categorized across three tiers:

**Natural and Accidental Risks**

- Earthquakes and submarine geological activity (Taiwan sits on the Pacific Ring of Fire)
- Typhoon-induced near-shore cable damage
- Fishing trawl and anchor strikes (accounting for approximately 60-70% of global submarine cable faults)
- Submarine landslides (the 2006 Hengchun earthquake severed multiple cables simultaneously)

**Gray Zone Threats**

- Deliberate sabotage disguised as "accidental" incidents
- Surveillance or interference of cables by unmanned underwater vehicles (UUVs)
- Intelligence gathering on submarine cable routing information
- Harassment operations targeting repair ships or landing stations

**Conflict Scenario Threats**

- Systematic severance: simultaneous destruction of multiple cables by submarines, mines, or special operations forces in a compressed timeframe
- Landing station strikes: precision attacks to destroy onshore terminal equipment
- Maritime blockade preventing repair vessels from accessing the area
- Electromagnetic pulse (EMP) effects on onshore relay stations

The 2006 Hengchun earthquake provides an important reference case. A magnitude 7.0 earthquake triggered submarine landslides that severed at least nine submarine cables, causing Taiwan's international internet bandwidth to plummet by over 90%. Full restoration took several weeks. This event demonstrated that the concentrated vulnerability of submarine cables is not a theoretical abstraction but a validated, real-world risk.

The vulnerability of outlying islands is even more pronounced. The Matsu Islands depend on only two submarine cables for their connection to Taiwan proper, and have experienced multiple incidents of weeks-long communications outages or degradation due to cable damage. In 2023, a Matsu submarine cable was severed by a cargo vessel's anchor, forcing approximately 14,000 residents to rely on microwave backup systems for communications over a period of several months — highlighting the fragility of outlying island communications infrastructure.

---

## 5.2 LEO Satellite Communications

### Background

Low Earth Orbit (LEO) satellite communications systems have achieved significant technological breakthroughs in recent years. Compared with traditional Geostationary Earth Orbit (GEO) satellites, LEO satellites offer the following advantages:

| Characteristic | GEO Satellites | LEO Satellites |
|----------------|---------------|---------------|
| Orbital altitude | ~35,786 km | 200-2,000 km |
| Communications latency | ~600 ms | ~20-40 ms |
| Per-satellite coverage | Large (~one-third of Earth's surface) | Small (requires constellation networking) |
| Launch and deployment cost | Very high | Moderate (mass production) |
| Survivability | Low (single point of failure has major impact) | High (distributed architecture) |

### Current Assessment

The global LEO satellite communications market is currently dominated by the following major systems:

- **Starlink (SpaceX)**: Has deployed over 6,000 satellites covering most of the globe. Demonstrated reliable communications capability in the Ukrainian theater of war, serving as a critical validation case for communications resilience under conflict conditions.
- **OneWeb (Eutelsat)**: Approximately 630 satellites deployed, with a focus on government and enterprise users.
- **Kuiper (Amazon)**: Planning 3,236 satellites; currently in early deployment stages.

Taiwan's current posture regarding LEO satellite communications includes:

1. **Commercial service introduction**: The Ministry of Digital Affairs has promoted the establishment of LEO satellite communication services in Taiwan, including assessments for cooperation with operators such as Starlink.
2. **Outlying island and remote area applications**: Outlying islands have begun testing satellite communications as a submarine cable backup.
3. **Defense application assessment**: The Ministry of National Defense continues to evaluate military satellite communications requirements, though indigenous capability remains limited.

### Analysis

The strategic significance of LEO satellite communications for Taiwan's communications resilience includes:

**Advantages**

- Provides an independent communications pathway that does not depend on submarine cables
- Distributed architecture is difficult to completely incapacitate through a single attack
- Ground terminal equipment can be rapidly deployed (compact antennas, low cost)
- The Ukraine experience has proven operational viability in an active conflict environment

**Limitations and Challenges**

- Bandwidth capacity is far below that of submarine cables (a single cable can carry tens of Tbps; overall satellite system bandwidth is limited)
- Commercial LEO systems are controlled by foreign corporations, and service availability is subject to geopolitical influence
- Ground terminal equipment can be jammed or geolocated through electronic warfare measures
- Advances in anti-satellite (ASAT) weapon technology pose a potential threat to LEO satellites
- Higher cost of satellite communications makes it impractical as a primary solution for everyday civilian communications

**Lessons from the Ukraine Experience**

During the Russia-Ukraine conflict, the Starlink system provided critical reference points in the following respects:

1. Rapidly restored basic communications capability in areas where traditional communications infrastructure had been destroyed
2. Supported military command and control and intelligence transmission
3. Maintained information flows between government institutions and civil society
4. Exposed the political risks of dependence on a single commercial provider (disputes over terms of service)

---

## 5.3 Backup Communications Architecture

### HF/UHF Radio Networks

High Frequency (HF, 3-30 MHz) and Ultra High Frequency (UHF, 300 MHz-3 GHz) radio communications represent the oldest long-distance communications technology, yet they continue to play an irreplaceable role in modern communications resilience frameworks.

**HF Radio Characteristics**

- Ionospheric reflection enables communication over thousands of kilometers without relay infrastructure
- Mature technology with low cost and easy maintenance
- Extremely low bandwidth (voice and low-speed data), unsuitable for large-scale data transfer
- Communications quality is volatile, affected by ionospheric conditions and solar activity

**UHF Radio Characteristics**

- Primarily line-of-sight communications, suitable for regional (tens of kilometers) coverage
- Higher bandwidth than HF, capable of supporting voice and medium-speed data transmission
- Requires relay stations to extend coverage
- Jamming resistance depends on adoption of frequency-hopping and spread-spectrum techniques

**Policy Direction**

A tiered HF/UHF backup communications network should be established nationwide:

| Tier | Function | Coverage | Operators |
|------|----------|----------|-----------|
| National | Central government external liaison | International | Military and diplomatic units |
| Regional | Inter-county/city government coordination | Island-wide | Government communications personnel at all levels |
| Local | Township/district emergency communications | Within county/city | Civil defense and fire service units |
| Amateur | Community communications support | Neighboring areas | Licensed amateur radio operators |

Taiwan currently has tens of thousands of licensed amateur radio operators. This community possesses latent communications support capability for disaster response. Regular exercises and institutional integration should be pursued to formally incorporate the amateur radio community into the national communications resilience framework.

### LoRa and Mesh Networks

**LoRa (Long Range) Technology**

LoRa is a Low-Power Wide-Area Network (LPWAN) technology with the following characteristics:

- Transmission range of 10-15 km (open terrain), approximately 2-5 km in urban environments
- Extremely low power consumption; battery-powered operation lasting months to years
- Very low bandwidth (suitable for sensor data and short text messages)
- Low device cost, suitable for large-scale deployment
- Open-source firmware such as Meshtastic enables infrastructure-free peer-to-peer communications

**Mesh WiFi Networks**

- Automatic node discovery and routing with self-healing network capability
- Failure of a single node does not affect overall network operation
- Coverage area expands as nodes are added
- Higher bandwidth than LoRa, capable of supporting basic web browsing and messaging
- Requires continuous power supply (higher power consumption compared to LoRa)

**Community-Level Communications Node Concept**

Under extreme scenarios — all submarine cables severed, satellite services restricted, mobile base stations disabled — community-level distributed communications nodes become the last line of defense for maintaining minimum communications capability. The recommended approach:

1. **Node deployment**: Deploy LoRa gateways and Mesh WiFi nodes at every village (li) or community activity center
2. **Power independence**: Pair with solar panels and battery energy storage systems to ensure operation even when disconnected from the grid
3. **Information transfer protocols**: Establish standardized emergency message formats, prioritizing transmission of personnel safety status, medical needs, and supply distribution information
4. **Community training**: Train community volunteers to operate and maintain communications equipment

### Multi-Layer Integration Architecture

The core principle of communications resilience is "defense in depth" — rather than relying on any single technology or piece of infrastructure, build a multi-layered backup structure that ensures graceful degradation rather than total failure.

**Multi-Layer Communications Resilience Architecture**

| Layer | Technology | Bandwidth | Coverage | Infrastructure Dependencies | Resilience Rating |
|-------|-----------|-----------|----------|---------------------------|------------------|
| Layer 1 | Submarine cables | Very high (Tbps-class) | Global | Cables, landing stations, terrestrial backbone | Low |
| Layer 2 | LEO satellites | Medium (Gbps-class) | Global | Ground terminals, satellite constellation | Medium-High |
| Layer 3 | HF/UHF radio | Very low (kbps-class) | Regional to global | Transmitters, antennas | High |
| Layer 4 | LoRa/Mesh | Very low to low | Community to regional | Node equipment, batteries | Very High |

Key design principles for this architecture:

1. **Graceful degradation**: When a high-bandwidth layer fails, automatic switchover to a lower-bandwidth but higher-resilience layer
2. **Functional prioritization**: When bandwidth is constrained, transmit in priority order: (a) military command and control, (b) government emergency coordination, (c) public safety information, (d) general communications
3. **Distributed control**: Control nodes at each layer are deployed in a distributed manner, preventing centralized management points from becoming attack targets
4. **Interoperability**: Standardized information exchange interfaces between layers ensure cross-layer message delivery

---

## 5.4 Policy Recommendations

Based on the foregoing analysis, the following policy recommendations are proposed:

**Short-Term Measures (1-2 Years)**

1. **Submarine cable risk assessment**: Commission an independent institution to conduct a comprehensive security assessment of existing submarine cables, including route analysis, landing station protection status, and repair capacity inventory.
2. **LEO satellite service procurement**: Enter into government-level service agreements with multiple LEO satellite communications operators to ensure priority bandwidth allocation during crises.
3. **Outlying island communications hardening**: Prioritize deployment of satellite communications and LoRa/Mesh backup systems on outlying islands.
4. **Amateur radio community integration**: Revise regulations to formally incorporate amateur radio operators into the national disaster response communications system.

**Medium-Term Measures (3-5 Years)**

5. **Submarine cable route diversification**: Invest in new submarine cables routed along paths different from existing ones (e.g., eastward toward the Pacific) to reduce route concentration risk.
6. **Landing station hardening**: Upgrade the physical protection level of submarine cable landing stations, including blast protection, EMP shielding, and backup power.
7. **National HF/UHF backup network**: Establish a tiered radio backup communications network covering the entire island, with regular live exercises.
8. **Community communications node pilot**: Launch a pilot program for community-level LoRa/Mesh communications node deployment in selected counties and cities.

**Long-Term Measures (5-10 Years)**

9. **Indigenous satellite communications capability**: Develop a nationally autonomous small satellite communications constellation to reduce dependence on foreign commercial systems (see Chapter 8 for details).
10. **Submarine cable monitoring system**: Deploy a subsea sensor network for real-time detection of cable anomalies and potential threat activity.
11. **Whole-of-society communications resilience**: Incorporate basic communications backup knowledge into all-out defense education and promote personal ownership and operation of backup communications equipment.
12. **Communications resilience legislation**: Enact legislation establishing resilience standards for communications infrastructure, requiring critical infrastructure operators to meet minimum backup requirements.

---

## References

1. International Telecommunication Union (ITU). *Submarine Cable Map and Statistics*. https://www.itu.int
2. TeleGeography. *Submarine Cable Map*. https://www.submarinecablemap.com
3. Chunghwa Telecom. Annual reports on submarine cable systems.
4. Ministry of Digital Affairs. Policy documents on communications infrastructure resilience.
5. Starlink Coverage Map and Service Documentation. https://www.starlink.com
6. Feldstein, S. (2022). "The Role of Satellite Internet in Ukraine." *Carnegie Endowment for International Peace*.
7. Ministry of Transportation and Communications. Regulations Governing Amateur Radio Operations.
8. LoRa Alliance. *LoRaWAN Specification*. https://lora-alliance.org
9. Meshtastic Project Documentation. https://meshtastic.org
10. National Communications Commission (NCC). Telecommunications infrastructure security assessment reports.
11. Bueger, C., & Liebetrau, T. (2023). "Protecting Undersea Cables: Challenges and Policy Options." *European Parliamentary Research Service*.
12. Institute for National Defense and Security Research. Research report on Taiwan's communications infrastructure security.

---

*(English translation)*
