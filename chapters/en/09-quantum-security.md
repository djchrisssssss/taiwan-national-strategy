# Chapter 9: Quantum Security — Post-Quantum Cryptography, QKD, and Long-Term Data Protection

> **Core Thesis**: Advances in quantum computing are steadily eroding the security foundations of existing cryptographic systems. Taiwan must complete its migration to post-quantum cryptography and establish quantum key distribution pilot programs before quantum computers acquire practical code-breaking capabilities, in order to safeguard national security, military communications, and the long-term confidentiality of the financial system.

---

## 9.1 The Quantum Computing Threat to Existing Cryptographic Systems

### Background

The foundations of modern information security rest on mathematical hard problems. RSA relies on the computational difficulty of large prime factorization; Elliptic Curve Cryptography (ECC) depends on the discrete logarithm problem; and the Diffie-Hellman key exchange is likewise grounded in discrete logarithms. On classical computers, these algorithms require astronomical amounts of computation to break and have therefore long been considered secure.

However, in 1994, Peter Shor demonstrated that a quantum computer with a sufficient number of qubits could perform large prime factorization and discrete logarithm computations in polynomial time. This means that mainstream public-key cryptographic systems such as RSA, ECC, and DH will no longer be secure in the quantum computing era.

| Encryption Algorithm | Classical Computing Difficulty | Quantum Computing Difficulty | Current Use Cases |
|---------------------|-------------------------------|-----------------------------|--------------------|
| RSA-2048 | Billions of years | Hours (theoretical) | TLS/SSL, digital signatures, email encryption |
| ECC-256 | Billions of years | Hours (theoretical) | Mobile communications, IoT, blockchain |
| AES-128 | Billions of years | Security halved (Grover's algorithm) | Data encryption, disk encryption, VPN |
| AES-256 | Billions of years | Retains 128-bit security | Military communications, highly classified data |

Symmetric encryption (such as AES) is relatively less affected by quantum computing. Grover's algorithm only improves brute-force search efficiency to the square root level, meaning AES-256 retains approximately 128-bit security strength in the quantum era. The threat to public-key cryptographic systems, however, is structural.

### The "Harvest Now, Decrypt Later" Attack Model

The quantum computing threat to encryption security is not confined to the future. The "Harvest Now, Decrypt Later" (HNDL) strategy is a known attack model already being executed. Its operational logic is as follows:

1. **Interception Phase**: State-level actors conduct mass interception and storage of encrypted communications, including diplomatic cables, military orders, financial transaction records, and internal government communications.
2. **Storage Phase**: Intercepted ciphertext is deposited into long-term storage facilities. At today's storage costs, the economic threshold for large-scale data retention is extremely low.
3. **Waiting Phase**: The adversary waits for quantum computing capabilities to mature to the scale required to execute Shor's algorithm.
4. **Decryption Phase**: Historical ciphertext is batch-decrypted using quantum computers to recover the original plaintext.

The danger of this strategy lies in the fact that even though quantum computers do not yet possess code-breaking capabilities, classified data transmitted today is already at risk. For information requiring long-term secrecy — military deployment plans, intelligence source identities, diplomatic strategies, infrastructure vulnerability assessments — HNDL attacks carry exceptionally high strategic value.

As a geopolitically sensitive actor, Taiwan's government communications, military command chains, and intelligence exchanges are priority targets for HNDL attacks. It is reasonable to assume that large-scale interception operations targeting Taiwan's communications are already underway.

### Timeline Pressure Assessment

The development timeline for quantum computing involves significant uncertainty, but the range of most expert estimates is narrowing:

| Timeframe | Quantum Computing Projection | Implications for Taiwan |
|-----------|-----------------------------|-----------------------|
| 2025-2028 | 1,000-10,000 logical qubits; error correction techniques reaching initial maturity | Cryptographic migration planning should be complete |
| 2028-2032 | Potentially reaching cryptographically relevant qubit scale | High-sensitivity systems should complete migration |
| 2032-2040 | Cryptanalytically capable quantum computers may become a reality | All critical systems must complete migration |

"Q-Day" — the date a quantum computer first successfully breaks mainstream public-key cryptography — is difficult to predict precisely. But cryptographic migration is a large-scale engineering effort requiring 5-15 years. If Q-Day arrives in 2035, then 2025 is already the critical initiation point for migration work.

The timeline pressure facing Taiwan can be conceptualized with the following formula:

**Migration Urgency = Data Secrecy Lifespan + Migration Duration - Time Remaining Until Q-Day**

If this value is positive, it is already too late to protect that category of data. For military and intelligence data requiring 30 years of secrecy, the window for initiating migration is critically narrow.

---

## 9.2 Post-Quantum Cryptography Migration

### The NIST Standardization Process

The U.S. National Institute of Standards and Technology (NIST) launched its Post-Quantum Cryptography (PQC) standardization process in 2016. After multiple rounds of evaluation, the first batch of standards was officially published in 2024:

| Standard | Algorithm Name | Type | Security Basis | Purpose |
|----------|---------------|------|---------------|---------|
| FIPS 203 | ML-KEM (formerly CRYSTALS-Kyber) | Key Encapsulation | Module Lattice Problem | Key exchange, encryption |
| FIPS 204 | ML-DSA (formerly CRYSTALS-Dilithium) | Digital Signature | Module Lattice Problem | Authentication, document signing |
| FIPS 205 | SLH-DSA (formerly SPHINCS+) | Digital Signature | Hash Functions | Backup signature scheme |

NIST continues to evaluate fourth-round candidate algorithms, including code-based schemes (such as BIKE and HQC). A diversified selection of algorithms reduces the systemic risk of a single mathematical assumption being broken.

### Taiwan's Migration Pathway

Taiwan's post-quantum cryptography migration should adopt a phased, risk-driven strategy:

**Phase One: Inventory and Assessment (12-18 months)**

- Conduct a comprehensive inventory of encryption algorithms and protocols used across government agencies, military units, and critical infrastructure.
- Establish a "Cryptographic Bill of Materials" (CBOM) documenting the cryptographic dependencies of each system.
- Perform risk classification based on data sensitivity and secrecy lifespan.
- Identify migration technical barriers, such as embedded systems, legacy hardware, and firmware constraints.

**Phase Two: Priority Migration (18-36 months)**

- Complete migration first for the highest-risk systems (military communications, intelligence exchanges, diplomatic cables).
- Adopt hybrid mode, running traditional algorithms alongside PQC algorithms simultaneously to ensure backward compatibility.
- Update TLS protocol stacks to support ML-KEM key exchange.
- Update digital signature infrastructure to support ML-DSA.

**Phase Three: Comprehensive Migration (36-72 months)**

- Extend to financial systems, telecommunications infrastructure, and civilian government systems.
- Update Public Key Infrastructure (PKI) root certificates and intermediate certificates.
- Develop industry migration guidelines to assist private-sector enterprises in synchronized upgrades.
- Establish continuous monitoring mechanisms to track quantum computing advances and the cryptographic security posture.

### Priority Protection Areas

Migration priorities across different domains should be determined by data sensitivity and secrecy lifespan:

| Priority Level | Domain | Data Secrecy Lifespan | Migration Target |
|---------------|--------|----------------------|-----------------|
| Highest | Military Command Communications | 30+ years | Complete by 2027 |
| Highest | Intelligence Sources and Methods | 50+ years | Complete by 2027 |
| High | Diplomatic Communications | 20-30 years | Complete by 2028 |
| High | Critical Infrastructure Control Systems | Real-time security | Complete by 2028 |
| Medium | Financial Trading and Settlement Systems | 7-10 years | Complete by 2030 |
| Medium | Healthcare Data | Lifetime protection | Complete by 2030 |
| Standard | Government Administrative Communications | 5-10 years | Complete by 2032 |
| Standard | Civilian Communications Infrastructure | 1-5 years | Complete by 2035 |

---

## 9.3 Quantum Key Distribution (QKD)

### Technical Principles and Limitations

Quantum Key Distribution leverages fundamental principles of quantum mechanics — specifically the Heisenberg uncertainty principle and the no-cloning theorem — to achieve theoretically unconditionally secure key exchange. The core concept is that any eavesdropping on the quantum channel will inevitably alter the quantum state, thereby being detected by both communicating parties.

Major QKD protocols include:

- **BB84 Protocol**: Encodes information using the polarization states of single photons; the earliest and most mature QKD scheme.
- **E91 Protocol**: Key distribution based on quantum entanglement, using Bell's inequality to verify security.
- **Continuous-Variable QKD (CV-QKD)**: Uses continuous variables of the optical field (such as amplitude and phase), offering better integration with existing fiber-optic infrastructure.

The technical limitations of QKD are equally significant and should not be overlooked:

| Limiting Factor | Description | Impact |
|----------------|-------------|--------|
| Distance limitation | Signal attenuation renders fiber-optic transmission unusable at approximately 100-300 km | Cannot directly cover the entire island |
| Key generation rate | Current commercial systems approximately 1-10 Mbps | Suitable only for key exchange, not data encryption |
| Infrastructure cost | Requires dedicated fiber-optic or free-space optical channels | High deployment costs |
| Trusted relay nodes | Long distances require relay stations, which themselves become security weak points | Reduces end-to-end security guarantees |
| Side-channel attacks | Hardware implementation flaws may be exploitable | Theoretical security does not equal practical security |

QKD should not be viewed as a replacement for PQC, but rather as a complement. PQC is a software-layer upgrade suitable for large-scale deployment; QKD is a physical-layer security mechanism suited for the highest-security point-to-point communications.

### Pilot Application Scenarios

Taiwan's geographic conditions — approximately 400 km from north to south, with major cities distributed along the western coast — are actually quite suitable for the gradual deployment of a QKD network. The recommended pilot plan is as follows:

**Short-Term Pilots (2026-2028)**

- **Taipei Metropolitan Government Secure Network**: A QKD-encrypted communications loop connecting the Presidential Office, Ministry of National Defense, National Security Bureau, and Executive Yuan. At distances of approximately 10-20 km, this is technically fully feasible.
- **Hsinchu Science Park Secure Link**: QKD-protected data transmission channels between highly sensitive semiconductor R&D facilities.

**Medium-Term Expansion (2028-2032)**

- **Taipei-Hsinchu-Taichung Backbone**: A QKD relay network built along highway fiber-optic corridors, covering major political and military nodes in the northern and central regions.
- **Military Command Chain Integration**: Incorporate QKD into tactical command communication backup systems, ensuring secure communication options remain available in electromagnetic contested environments.

**Long-Term Vision (Post-2032)**

- **Island-wide QKD Backbone Network**: Integrate quantum repeater technology (pending technical maturation) to achieve island-wide coverage.
- **Satellite QKD**: Explore satellite quantum communication links in cooperation with friendly nations to overcome ground-based distance limitations. China launched the Micius quantum science experimental satellite in 2016; Taiwan should not be absent from this domain.

---

## 9.4 Policy Recommendations

### Organization and Governance

1. **Establish a National Quantum Security Office**: Create an inter-ministerial coordination mechanism at the Executive Yuan level to oversee post-quantum cryptography migration, QKD deployment, and quantum technology R&D policy. This office should possess sufficient authority and budget allocation power, rather than serving merely in an advisory capacity.

2. **Mandate Crypto-Agility Requirements**: Require all newly built and upgraded government information systems to possess crypto-agility — the ability to replace encryption algorithms without rebuilding the system. This requirement should be incorporated into government IT procurement regulations.

3. **Publish a National Cryptographic Migration Timeline**: Following the framework of the U.S. National Security Memorandum (NSM-10), issue a Taiwan-specific post-quantum cryptography migration timeline that clearly specifies migration deadlines and responsibilities for each agency.

### Technology Investment

4. **Fund Post-Quantum Cryptography Research**: Through the National Science and Technology Council (NSTC) and Academia Sinica, expand PQC research funding, with particular focus on:
   - Performance optimization of PQC algorithms on hardware platforms commonly used in Taiwan.
   - Security analysis of hybrid encryption schemes.
   - Integration testing of PQC with existing systems.

5. **Develop Domestic QKD Technical Capacity**: Support collaboration between domestic academic and research institutions and industry in developing QKD equipment and systems to avoid complete dependence on foreign suppliers. Supply chain security for critical equipment must be factored into planning.

6. **Build a Quantum Security Testing and Validation Platform**: Provide an environment for government agencies and enterprises to test PQC algorithm compatibility and performance, accelerating the migration process.

### International Cooperation

7. **Participate in International Standards Development**: Actively engage in the post-quantum cryptography and QKD standards development processes of international organizations such as NIST, ETSI, and ISO to ensure Taiwan's technical requirements and use cases are taken into consideration.

8. **Establish Bilateral Quantum Security Partnerships**: Build cooperation mechanisms with partners leading in quantum technology — including the United States, Japan, and the European Union — covering technical exchanges, joint research, and security assessments.

9. **Immediate Data Protection Actions**: For the most highly classified data currently in transit that requires long-term secrecy, hybrid encryption schemes (traditional algorithms + PQC algorithms) should be adopted immediately, without waiting for comprehensive migration to be completed. This is the lowest-cost, highest-benefit immediate protective measure.

### Talent Development

10. **Build a Quantum Cybersecurity Talent Pipeline**: Add post-quantum cryptography courses to university computer science and cybersecurity programs, and cultivate professionals with practical migration experience through industry-academic partnership programs. Taiwan is estimated to need at least 500-1,000 cybersecurity engineers with PQC expertise over the next decade.

---

## References

- NIST. "Post-Quantum Cryptography Standardization." National Institute of Standards and Technology, 2024. https://csrc.nist.gov/projects/post-quantum-cryptography
- Shor, P.W. "Algorithms for Quantum Computation: Discrete Logarithms and Factoring." *Proceedings of the 35th Annual Symposium on Foundations of Computer Science*, 1994.
- National Security Agency. "Quantum Computing and Post-Quantum Cryptography FAQ." NSA Cybersecurity, 2021.
- European Telecommunications Standards Institute. "Quantum Safe Cryptography and Security." ETSI White Paper No. 8, 2015.
- Chen, L. et al. "Report on Post-Quantum Cryptography." NISTIR 8105, National Institute of Standards and Technology, 2016.
- Mosca, M. "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?" *IEEE Security & Privacy*, vol. 16, no. 5, 2018, pp. 38-41.
- White House. "National Security Memorandum on Promoting United States Leadership in Quantum Computing While Mitigating Risks to Vulnerable Cryptographic Systems (NSM-10)." May 2022.
- Liao, S.K. et al. "Satellite-to-ground quantum key distribution." *Nature*, vol. 549, 2017, pp. 43-47.
- Executive Yuan Department of Cyber Security. *National Cybersecurity Development Plan*. 2021.
- Academia Sinica. *Recommendations on Quantum Science and Technology Research and Development*. 2022.

---

*(English translation)*
