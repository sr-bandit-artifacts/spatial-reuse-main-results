// SPDX-License-Identifier: GPL-2.0-only
// Copyright (c) 2026 sr-bandit-artifacts
// See LICENSE in this directory for the full license text.

#ifndef __BRIDGE_UTILS_HH
#define __BRIDGE_UTILS_HH

#include <string>

namespace BridgeUtils {
	bool sendAll(int fd, const std::string& payload);
	bool receiveLine(int fd, std::string& line, unsigned int maxBytes = 1024 * 1024);
	bool connectTcp(const std::string& host, const std::string& port, int& fd, std::string& error);
}

#endif
