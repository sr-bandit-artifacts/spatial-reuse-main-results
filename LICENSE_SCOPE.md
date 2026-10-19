# License scope

This repository contains components with different licenses. The copyright
holder for the project-authored contributions is identified publicly by the
GitHub account `sr-bandit-artifacts`. Existing third-party copyright notices
and license terms remain in force.

| Component | Applicable license |
| --- | --- |
| Project-authored Python files in `scripts/` and `code/neural_bandit_bridge/` | MIT; see [LICENSE](LICENSE) and the file headers |
| Project-authored configuration files in `configs/`, topology JSON files in `code/nsTest/topos/`, and repository documentation | MIT; see [LICENSE](LICENSE) |
| Native simulator C++ files in `code/nsTest/`, except the JsonCpp files below | GPL-2.0-only; see [code/nsTest/LICENSE](code/nsTest/LICENSE) and the file headers |
| ns-3 patches in `code/patches/` | GPL-2.0-only; see [code/patches/LICENSE](code/patches/LICENSE) |
| JsonCpp: `code/nsTest/json.hh`, `json-forwards.hh`, and `jsoncpp.cc` | Original public-domain/MIT terms embedded in those files |
| Bundled ns-3 and other upstream components in `code/vendor/` | Their original licenses; ns-3 uses GPLv2; see [code/NOTICE.txt](code/NOTICE.txt) and the notices inside the archive |
| Measurements, model checkpoints, figures and tables in `results/` | Outside this source-code license grant; existing rights are retained |

The MIT grant does not replace the licenses of the GPL or third-party
components. Distribution of a combined ns-3 simulator must follow the
applicable GPL terms. The separately executed Python controllers retain their
MIT license.

## Attribution and research citation

When redistributing MIT-covered code or substantial portions of it, retain its
copyright notice and the complete MIT license. Retain the relevant copyright
and license notices for GPL and third-party components as well, and follow
their distribution requirements.

For research using this software, please cite [CITATION.cff](CITATION.cff),
identify the commit used, and describe your modifications. Academic citation
is requested separately from the license conditions; this request does not
add a restriction to the standard MIT or GPL licenses.
