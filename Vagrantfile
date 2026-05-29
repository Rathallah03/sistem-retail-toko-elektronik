Vagrant.configure("2") do |config|

  # =========================
  # VM DATABASE
  # =========================
  config.vm.define "vm-database" do |db|
    db.vm.box = "bento/ubuntu-22.04"
    db.vm.hostname = "vm-database"

    db.vm.network "private_network", ip: "192.168.56.11"

    db.vm.provider "virtualbox" do |vb|
      vb.name = "VM-Database-Retail"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # =========================
  # VM BACKEND
  # =========================
  config.vm.define "vm-backend" do |backend|
    backend.vm.box = "bento/ubuntu-22.04"
    backend.vm.hostname = "vm-backend"

    backend.vm.network "private_network", ip: "192.168.56.10"

    backend.vm.provider "virtualbox" do |vb|
      vb.name = "VM-Backend-Retail"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

  # =========================
  # VM FRONTEND
  # =========================
  config.vm.define "vm-frontend" do |frontend|
    frontend.vm.box = "bento/ubuntu-22.04"
    frontend.vm.hostname = "vm-frontend"

    frontend.vm.network "private_network", ip: "192.168.56.12"

    frontend.vm.provider "virtualbox" do |vb|
      vb.name = "VM-Frontend-Retail"
      vb.memory = "1024"
      vb.cpus = 1
    end
  end

end